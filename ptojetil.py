import pygame
import math
import random



class shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/tiro.png")
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect =  self.image.get_rect()




        self.speed = 4

    def update(self, *args):

        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()


