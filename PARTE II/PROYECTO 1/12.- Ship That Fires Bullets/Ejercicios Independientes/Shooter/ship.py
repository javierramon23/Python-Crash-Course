import pygame

class Ship():
    # screen como parámetro por que trabajaremos con la PANTALLA DENTRO D LA CLASE
    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ship_image = pygame.image.load('../images/ship.bmp')
        self.ship_rect = self.ship_image.get_rect()

        self.ship_rect.

    def blit_me(self):
        self.screen.blit(self.ship_image, self.ship_rect)

