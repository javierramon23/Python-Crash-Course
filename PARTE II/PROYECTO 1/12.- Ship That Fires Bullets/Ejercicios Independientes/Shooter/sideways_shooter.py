import sys
import pygame
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group

def fire_bullet(screen, ship):
    new_bullet = Bullet(screen, ship)
    return new_bullet

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption('Sideways Shooter')

    ship = Ship(screen)
    
    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ship.move_up = True
                elif event.key == pygame.K_DOWN:
                    ship.move_down = True
                elif event.key == pygame.K_SPACE:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ship.move_up = False
                elif event.key == pygame.K_DOWN:
                    ship.move_down = False
                elif event.key == pygame.K_SPACE:
                    print('ALTO EL FUEGO!!')

        screen.fill((230, 230, 230))
        ship.update()
        ship.blit_me()
        
        pygame.display.flip() 

run_game()