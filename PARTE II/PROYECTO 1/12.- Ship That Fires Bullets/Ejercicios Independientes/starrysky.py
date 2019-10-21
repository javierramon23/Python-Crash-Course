# Se IMPORTAN LAS LIBRERIAS NECESARIAS PARA LA APP.
import pygame   #
import sys      #
from pygame.sprite import Group #
import game_functions as gf     #


def run_game():

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Starry Sky')

    stars = Group()
    
    gf.create_constellation(screen, stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
        screen.fill((255,255,250))
        stars.draw(screen)
        pygame.display.flip()


run_game()
    