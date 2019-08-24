import pygame
from pygame.sprite import Sprite
"""
    Clase SPRITE:
    Suele usarse como BASE para diferentes OBJETOS
    Los SPRITES permiten AGRUPAR ELEMENTOS QUE ESTEN RELACIONADOS
    y ACTUAR SOBRE TODOS ELLOS de UNA VEZ.
"""
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """
            Se LLAMA al CONSTRUCTOR de la CLASE PADRE 'Sprite':
        """
        # SINTAXIS Python2.7:
        # super(Bullet, self).__init__()
        # SINTAXIS Python3:
        super().__init__()

        self.screen = screen
        # Creamos un RECTANGULO que REPRESENTARA UNA BALA.
        self.bullet_rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        # Ponemos la BALA en su POSICION, ENCIMA DE LA PUNTA DE LA NAVE
        self.bullet_rect.centerx = ship.rect.centerx
        self.bullet_rect.top = ship.rect.top

        # El ATRIBUTO 'y' del los OBJETOS TIPO 'rect' SOLO ALMACENAN VALORES ENTEROS
        # es necesario trabajar con otra VARIABLE para poder TRABAJAR con VALORES FLOAT
        # PARA TRABAJAR CON MAS PRECISION CON LA VELOCIDAD D DESPLAZAMIENTO
        self.bullet_y = float(self.bullet_rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """ MOVEMOS la BALA HACIA LA PARTE SUPERIOR DE LA PANTALLA """
        # ACTUALIZAMOS LA POSICION DECIMAL
        self.bullet_y -= self.speed_factor
        # ACTUALIZAMOS LA POSION DEL RECTANGULO(SUPERFICIE) DE LA BALA
        self.bullet_rect.y = self.bullet_y

    def draw_bullet(self):
        """ DIBUJAMOS LA BALA EN LA PANTALLA """
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)