import pygame

class Ship():
    def __init__(self, screen):
        """ CONSTRUCTOR DE LA CLASE SHIP"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('../images/ship.bmp')
        self.ship_rect = self.ship.get_rect()

        # POSICIONAMOS LA NAVE EN EL CENTRO DE LA PANTALLA(X,Y)
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.centery = self.screen_rect.centery

        # SE CREAN UNAS 'FLAG' PARA COMPROBAR DESPLAZAMIENTO DE LA NAVE
        # SI EL 'FLAG' ESTA A 'FALSE', LA NAVE NO SE DESPLAZA EN ESA DIRECCION
        # SI ESTA a 'TRUE' SE ESTA MOVIENDO.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_position(self):
        """ 
            COMPROBAMOS LOS 'FLAGS' DE MOVIMIENTO Y SE DESPLAZA O NO, TAMBIEN
            COMPROBAMOS LOS LIMITES DE LA PANTALLA PARA QUE NO DESAPAREZCA.

            !!IMPORTANTE!!: La ESQUINA SUPERIOR IZQUIERDA DE LA PANTALLA REPRESENTA
            LAS COORDENADAS (0,0)
        """
        if self.moving_up and self.ship_rect.top > self.screen_rect.top:
            self.ship_rect.centery -= 5
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.centery += 5
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_rect.centerx += 5
        if self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.ship_rect.centerx -= 5

    def blit_ship(self):
        """ METODO QUE DIBUJA LA NAVE EN PANTALLA """
        self.screen.blit(self.ship, self.ship_rect)
