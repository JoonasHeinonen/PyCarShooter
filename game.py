import pygame
import sys
from player import Player
from row import Row
from projectile import Projectile

pygame.init()

MAP_SIZE = 500

win = pygame.display.set_mode((MAP_SIZE, MAP_SIZE))

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

x = 250
y = 250
width = 40
height = 70
vel = 5

# DEFINITION OF OBJECTS

player = Player(x, y, width, height)

row0 = Row(245, 0, 10, 60)
row1 = Row(245, 280, 10, 60)

bullets = []

# FUNCTIONS

def redrawGameWindow():
    # Background / Road 
    win.fill((0, 160, 0))
    pygame.draw.rect(win, (100, 100, 100), (50, 0, (400), MAP_SIZE))
    pygame.draw.rect(win, (255, 255, 255), (55, 0, (10), MAP_SIZE))
    pygame.draw.rect(win, (255, 255, 255), (435, 0, (10), MAP_SIZE))
    row0.draw(win)
    row1.draw(win)
    player.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# mainloop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y > (player.y - 500):
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        sys.exit()

    if keys[pygame.K_RCTRL]:
        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + (-10) // 2), 5, (255, 255, 0), 1))

    if keys[pygame.K_LEFT] and player.x > 50:
        player.x -= vel
    if keys[pygame.K_RIGHT] and player.x < 410:
        player.x += vel        
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= vel        
    if keys[pygame.K_DOWN] and player.y < 430:
        player.y += vel

    row0.y += vel
    row1.y += vel
    
    if (row0.y > MAP_SIZE):
        row0.y = -60
    if (row1.y > MAP_SIZE):
        row1.y = -60

    redrawGameWindow()
    

pygame.quit()