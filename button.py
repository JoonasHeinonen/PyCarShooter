import pygame

class Button:
    """A class that provides a button GUI element."""

    def __init__(self, color, x, y, width, height, text='', text_color=(0, 0, 0), font_size=30):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.font_size = font_size

    def draw_button(self, win):
        """Draws the button on the given window."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.text != '':
            font = pygame.font.SysFont('arial', self.font_size)
            text = font.render(self.text, True, self.text_color)
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))