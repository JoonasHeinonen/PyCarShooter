import pygame

class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

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