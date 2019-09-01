import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # CONSTRUCToR DE LA SUPERCLASE SPRITE.
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        '''
        Para poder utilizar el METODO 'draw()' de un OBJETO 'Group()'
        los OBJETOS que CONTENGA ese GRUPO DEBEN DEFINIR OBLIGATORIAMIENTE
        LOS ATRIBUTOS 'image' y 'rect', por eso CAMBIAMOS los NOMRES 'alien_image' y 'alien_rect'
        en ESTA CLASE.

        self.alien_image = pygame.image.load('images/alien.bmp')
        self.alien_rect = self.alien_image.get_rect()

        self.alien_rect.x = self.alien_rect.width
        self.alien_rect.y = self.alien_rect.height

        self.x = float(self.alien_rect.x)
        '''
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    #def blitme(self):
        #self.screen.blit(self.alien_image, self.alien_rect)
