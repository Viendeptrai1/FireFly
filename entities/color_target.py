import pygame
import random
from utils.colors import COLORS

WIDTH = 800
HEIGHT = 600

class ColorTarget(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 30)
        self.color_name = [name for name, rgb in COLORS.items() if rgb == color][0]