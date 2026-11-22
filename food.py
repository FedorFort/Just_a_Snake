import pygame
import random

class Food:
    def __init__(self, size, screen_width, screen_height, cell):
        self.size = size
        self.cell = cell
        self.cols = screen_width // cell
        self.rows = screen_height // cell
        self.color = (200, 200, 100)
        self.rect = pygame.Rect(0, 0, size, size)
        self.respawn([])

    def respawn(self, forbidden):
        offset = (self.cell - self.size) // 2
        for _ in range(100):
            x = random.randrange(self.cols) * self.cell + offset
            y = random.randrange(self.rows) * self.cell + offset
            self.rect.topleft = (x, y)
            if self.rect.collidelist(forbidden) == -1:
                return

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)