import sys
import pygame
from ship import Ship

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300,400))
    pygame.display.set_caption('Sideways Shooter')

    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('ARRIBA')
                elif event.key == pygame.K_DOWN:
                    print('ABAJO')
                elif event.key == pygame.K_SPACE:
                    print('FUEGO!!')
            if event.type == pygame.KEYUP:
                print('Tecla Levantada')

        screen.fill((230, 230, 230))
        ship.blit_me()
        pygame.display.flip() 

run_game()