import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self,screen):

        super().__init__()

        self.screen = screen
        self.image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()
