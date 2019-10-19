import pygame
import random
from player import Player
from projectile import Projectile

class Enemy(object):
    # Colors
    blue = (0, 0, 180)
    red = (180, 0, 0)
    green = (0, 180, 0)
    black = (0, 0, 0)

    carColor = blue
    beepLoop = 0
    isPoliceCar = False
    light1 = blue
    light2 = red

    def __init__(self, y, player):
        self.x = self.getNewX()
        self.y = y
        self.player = player
        self.width = 40
        self.height = 70
        self.vel = 5
        self.hitbox = (self.x, self.y, 39, 69)
        self.health = 1
        self.visible = True
        self.carColor = self.setColor()
        self.isPoliceCar = self.randPolice()

    def randPolice(self):
        rand = random.randrange(0, 2)
        if (rand == 0):
            print(0)
            return False
        elif (rand == 1):
            print(1)
            return True
        return False

    def draw(self, win):
        self.move()
        if self.visible:
            if (self.isPoliceCar == False):
                pygame.draw.rect(win, self.carColor, (self.x , self.y, (self.width), self.height))
            elif (self.isPoliceCar == True):
                pygame.draw.rect(win, (0, 0, 0), (self.x , self.y, (self.width), self.height))                
            pygame.draw.rect(win, (255, 255, 0), (self.x, self.y + 68, (self.width - 30), self.height - 68))
            pygame.draw.rect(win, (255, 255, 0), (self.x + 30, self.y + 68, (self.width - 30), self.height - 68))
            pygame.draw.rect(win, (0, 0, 255), (self.x + 1, self.y + 5, (self.width - 2), self.height - 20))
            if (self.isPoliceCar == False):
                pygame.draw.rect(win, self.carColor, (self.x + 1, self.y + 10, (self.width - 2), self.height - 35))
            elif (self.isPoliceCar == True):
                pygame.draw.rect(win, (255, 255, 255), (self.x + 1, self.y + 10, (self.width - 2), self.height - 35))         
                pygame.draw.rect(win, (140, 140, 140), (self.x +4, self.y + 22, (self.width - 8), self.height - 60))
                pygame.draw.rect(win, self.light1, (self.x + 4, self.y + 22, (self.width - 28), self.height - 60))
                pygame.draw.rect(win, self.light2, (self.x + 24, self.y + 22, (self.width - 28), self.height - 60))
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, (self.width - 30), self.height - 68))
            pygame.draw.rect(win, (255, 0, 0), (self.x + 30, self.y, (self.width - 30), self.height - 68))
            self.hitbox = (self.x, self.y, 39, 69)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.health = 1
            self.respawn()

    def move(self):
        if (self.isPoliceCar == False):
            self.y += self.vel * 1.1
        elif (self.isPoliceCar == True):
            self.y += self.vel * 1.5

        if (self.y > 500):
            self.respawn()

        if self.isPoliceCar:
            self.beepLoop += 1
            if self.beepLoop > 14:
                self.beepLoop = 0

            if (self.beepLoop == 0):
                self.light1 = self.red
                self.light2 = self.blue
            elif (self.beepLoop == 7):
                self.light1 = self.blue
                self.light2 = self.red

    def respawn(self):
        self.isPoliceCar = self.randPolice()
        self.health = 1
        self.carColor = self.setColor()
        self.y = self.getNewY()
        self.x = self.getNewX()

    def setColor(self):
        rand = random.randrange(0, 4)
        if rand == 0:
            return self.blue
        elif rand == 1:
            return self.red
        elif rand == 2:
            return self.green
        elif rand == 3:
            return self.black
    
    def getNewX(self):
        x = random.randrange(50, 400)
        return x
    
    def getNewY(self):
        y = random.uniform(-70, -500)
        return y