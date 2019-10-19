import pygame
import sys
from player import Player
from enemy import Enemy
from row import Row
from projectile import Projectile

pygame.init()

MAP_SIZE = 500

win = pygame.display.set_mode((MAP_SIZE, MAP_SIZE))

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

# States

start = False
gameOver = False

# Sounds

gunSound = pygame.mixer.Sound('sounds/gun.wav')
hitSound = pygame.mixer.Sound('sounds/hit.wav')
destroyedSound = pygame.mixer.Sound('sounds/destroyed.wav')

# music = pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)

score = 0

x = 250
y = 250
width = 40
height = 70
vel = 5

# DEFINITION OF OBJECTS

player = Player(x, y)

enemy0 = Enemy(-140, player)
enemy1 = Enemy(-140, player)
enemy2 = Enemy(-140, player)

row0 = Row(245, 0, 10, 60)
row1 = Row(245, 280, 10, 60)

shootLoop = 0
bullets = []
enemies = [enemy0, enemy1, enemy2]

# FUNCTIONS

def redrawGameWindow():
    # Background / Road 
    win.fill((0, 160, 0))
    text = scoreNormalFont.render('Score: ' + str(score), 1, (0, 0, 0))
    pressSpaceToPlay = scoreNormalFont.render('Press Space to play!', 1, (255, 255, 255))
    scoreText = scoreNormalFont.render('Your score: ' + str(score), 1, (255, 255, 255))
    pygame.draw.rect(win, (100, 100, 100), (50, 0, (400), MAP_SIZE))
    pygame.draw.rect(win, (255, 255, 255), (55, 0, (10), MAP_SIZE))
    pygame.draw.rect(win, (255, 255, 255), (435, 0, (10), MAP_SIZE))
    row0.draw(win)
    row1.draw(win)
    if (start == False and gameOver == False):
        win.blit(pressSpaceToPlay, (175, 245))
    elif (start == True and gameOver == False):
        for bullet in bullets:
            bullet.draw(win)
        enemy0.draw(win)
        if (score > 10):
            enemy1.draw(win)
        if (score > 50):
            enemy2.draw(win)
        player.draw(win)
        win.blit(text, (10, 10))
    elif (start == False and gameOver == True):
        player.x = -500
        player.y = 800
        win.blit(scoreText, (195, 245))
        win.blit(pressSpaceToPlay, (175, 210))
    pygame.display.update()

# mainloop
scoreNormalFont = pygame.font.SysFont('arial', 16, True, True)

run = True
while run:
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if (start == True):
        for enemy in enemies:
            if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3]> enemy.hitbox[1]:
                    if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                        destroyedSound.play()
                        enemy.respawn()
                        player.hit()

        if shootLoop > 0:
            shootLoop += 0.25
        if shootLoop > 5:
            shootLoop = 0

        for bullet in bullets:
            for enemy in enemies:
                if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                    if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        enemy.hit()
                        hitSound.play()
                        score += 1
                        bullets.pop(bullets.index(bullet))
                        if (enemy.health == 0):
                            score += 3
                            if (enemy.isPoliceCar == True):
                                score += 5

            if bullet.y > 0:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if keys[pygame.K_ESCAPE]:
            sys.exit()

        if keys[pygame.K_RCTRL] and shootLoop == 0:
            gunSound.play()
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + (-10) // 2), 5, (255, 255, 0), 1))
            shootLoop = 1

        if keys[pygame.K_LEFT] and player.x > 50:
            player.x -= vel
        if keys[pygame.K_RIGHT] and player.x < 410:
            player.x += vel        
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= vel        
        if keys[pygame.K_DOWN] and player.y < 430:
            player.y += vel

        if (player.health == 0):
            enemy1.x = 1000
            enemy1.y = 1000
            enemy2.x = 1000
            enemy2.y = 1000
            player.x = 3000
            player.y = 3000
            start = False
            gameOver = True

    if (gameOver == True):
        if keys[pygame.K_SPACE]:
            start = True
            gameOver = False
            player.x = x
            player.y = y
            player.health = 6
            score = 0

    row0.y += vel
    row1.y += vel
    
    if (row0.y > MAP_SIZE):
        row0.y = -60
    if (row1.y > MAP_SIZE):
        row1.y = -60

    redrawGameWindow()
    

pygame.quit()