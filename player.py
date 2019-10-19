import pygame
import random
import sys

class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 70
        self.health = 6
        self.vel = 5
        self.hitbox = (self.x, self.y, 39, 69)

    def draw(self, win):
        pygame.draw.rect(win, (0, 150, 255), (self.x , self.y, (self.width), self.height))
        pygame.draw.rect(win, (255, 255, 255), (self.x + 28, self.y, (self.width - 56), self.height))
        pygame.draw.rect(win, (0, 150, 255), (self.x + 15, self.y, (self.width - 30), self.height))
        pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, (self.width - 30), self.height - 68))
        pygame.draw.rect(win, (255, 255, 0), (self.x + 30, self.y, (self.width - 30), self.height - 68))
        pygame.draw.rect(win, (0, 0, 255), (self.x + 1, self.y + 20, (self.width - 2), self.height - 30))
        pygame.draw.rect(win, (0, 150, 255), (self.x + 1, self.y + 30, (self.width - 2), self.height - 50))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y + 68, (self.width - 30), self.height - 68))
        pygame.draw.rect(win, (255, 0, 0), (self.x + 30, self.y + 68, (self.width - 30), self.height - 68))
        self.hitbox = (self.x, self.y, 39, 69)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), (180, 0, (140), 10))
        pygame.draw.rect(win, (0, 255, 0), (180, 0, self.width - ((self.width / 2) * (1 - self.health)), 10 ))


    def hit(self):
        if self.health > 0:
            self.health -= 1
            self.x = self.getNewX()
            self.y = 410

    def getNewX(self):
        x = random.randrange(50, 400)
        return x