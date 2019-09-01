import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):
        
        super().__init__()

        self.screen = screen

        self.bullet_rect = pygame.Rect(0,0,6,3)
        self.bullet_color = (0,0,0)
        self.bullet_speed = 10

        self.bullet_rect.midleft = ship.ship_rect.midright

    def update(self):
        self.bullet_rect.x += self.bullet_speed

    def draw_me(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rect)