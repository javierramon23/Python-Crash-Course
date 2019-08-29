import pygame

class Ship():
    # screen como parámetro por que trabajaremos con la PANTALLA DENTRO D LA CLASE
    def __init__(self, screen):
        
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ship_image = pygame.image.load('../images/ship.bmp')
        self.ship_image = pygame.transform.rotate(self.ship_image, -90)
        self.ship_rect = self.ship_image.get_rect()

        self.ship_rect.centery = self.screen_rect.centery

        self.ship_speed = 10
        self.move_up = False
        self.move_down = False
    
    def update(self):
        if self.move_up and self.ship_rect.top > self.screen_rect.top:
            self.ship_rect.centery -= self.ship_speed
        if self.move_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.centery += self.ship_speed

    def blit_me(self):
        self.screen.blit(self.ship_image, self.ship_rect)

