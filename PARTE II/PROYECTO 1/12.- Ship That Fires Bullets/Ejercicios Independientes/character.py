import pygame

class Character():
    """CONSTRUCTOR"""
    def __init__(self, screen):
        self.screen = screen

        # SE CARGA LA IMAGEN
        self.image = pygame.image.load('images/ball.jpg')
        """
            PARA POSICIONAR LA IMAGEN DENTRO DE LA PANTALLA EN UN LUGAR CONCRETO
            SE UTILIZA EL METODO 'get_rect()' QUE DEVUELVE UN RECTANGULO QUE PUEDE
            DECIRNOS LAS DIMENSIONES Y LOCALIZACION DE UN OBJETO (SUPERFICIE QUE OCUPA)
        """
        self.rect_image = self.image.get_rect()
        self.rect_screen = self.screen.get_rect()
        """
            POSICIONAMOS LA IMAGEN, EL RECTANGULO DEVUELTO POR 'get_rect()'
            EN LA PARTE CENTRAL DE LA VENTANA.
            SE UTILIZAN UNA SERIE DE METODOS DEL OBJETO DEVUELTO POR 'get_rect()'
        """
        self.rect_image.centerx = self.rect_screen.centerx
        self.rect_image.centery = self.rect_screen.centery

    def blit_me(self):
        """DIBUJAMOS LA IMAGEN EN EL BUFFER DE LA PANTALLA EN UNA POSICION ESPECIFICADA"""
        self.screen.blit(self.image, self.rect_image)