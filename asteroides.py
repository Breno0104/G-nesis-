import pygame
import math
import random

class asteroide(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/aste1.png")
        self.image = pygame.transform.scale(self.image, [120, 120])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(2, 400)


        self.speed = 2 + random.random() * 2

    def update(self, *args):

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()







