import pygame
import os

WIDTH = 800
HEIGHT = 600

class Firefly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image = pygame.image.load(os.path.join(current_dir, 'assets', 'domdom.png'))
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 4

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))