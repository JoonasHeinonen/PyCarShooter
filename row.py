import pygame

class Row(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x , self.y, (self.width), self.height))