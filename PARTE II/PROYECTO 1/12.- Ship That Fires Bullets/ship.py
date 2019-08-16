import pygame

class Ship():
    """ """
    def __init__(self, ai_settings, screen):
        # Para poder TRABAJAR con la VENTANA de la PANTALLA PRINCIPAL del juego.
        self.screen = screen

        # Para poder TRABAJAR con las PROPIEDADES INICIAlES del JUEGO.
        self.ai_settings = ai_settings

        # CARGA la IMAGEN de la NAVE.
        self.image = pygame.image.load('images/ship.bmp')
        # DEVUELVE el 'RECTANGULO que ENVUELVE' a la IMAGEN.
        self.rect = self.image.get_rect()
        # DEVUELVE el 'RECTANGULO que ENVUELVE' a la VENTANA.
        self.screen_rect = self.screen.get_rect()

        # POSICIONAMOS LA NAVE EN LA PARTE INFERIOR CENTRAL DE LA VENTANA.
        # IGUALANDO la POSICION CENTRAL del RECTANGULO de la VENTANA con el RECTANGULO de la IMAGEN. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Controla si la Nave esta en MOVIMIENTO (CURSOR PULSADO = TRUE)
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ ACTUALIZA LA POSICION EN FUNCION DE LAS VARIABLES DE MOVIMIENTO """
        # Si la VARIABLE es True, la NAVE se MUEVE a la DERECHA.
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        # Si la VARIABLE es True, la NAVE se MUEVE a la IZQUIERDA.
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        ''' Dibujamos la NAVE en su POSICION'''
        # 2 PARAMETROS: QUE DIBUJAMOS y DONDE lo DIBUJAMOS.
        self.screen.blit(self.image, self.rect)
    



