import sys
import pygame

def game_run():
    pygame.init()
    """ SCREEN SETTINGS """
    screen = pygame.display.set_mode((250,100))
    pygame.display.set_caption('Captura el Evento')

    """ PYGAME MAIN LOOP"""
    while True:
        """ EVENT LOOP """
        for event in pygame.event.get():
            """ TYPE EVENTS"""
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print('Tecla Pulsada: {}'.format(chr(event.key)))

        """ UPDATE SCREEN """
        screen.fill((255, 255, 255))       
        pygame.display.flip()

game_run()