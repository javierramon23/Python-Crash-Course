import pygame

class Ship():

    def __init__(self, screen):
        # Para poder TRABAJAR con la VENTANA de la PANTALLA PRINCIPAL del juego.
        self.screen = screen

        # CARGA la IMAGEN de la NAVE.
        self.image = pygame.image.load('images/ship.bmp')
        # DEVUELVE el 'RECTANGULO que ENVUELVE' a la IMAGEN.
        self.rect = self.image.get_rect()
        # DEVUELVE el 'RECTANGULO que ENVUELVE' a la VENTANA.
        self.screen_rect = screen.get_rect()

        # POSICIONAMOS LA NAVE EN LA PARTE INFERIOR CENTRAL DE LA VENTANA.
        # IGUALANDO la POSICION CENTRAL del RECTANGULO de la VENTANA con el RECTANGULO de la IMAGEN. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        ''' Dibujamos la NAVE en su POSICION'''
        # 2 PARAMETROS: QUE DIBUJAMOS y DONDE lo DIBUJAMOS.
        self.screen.blit(self.image, self.rect)


