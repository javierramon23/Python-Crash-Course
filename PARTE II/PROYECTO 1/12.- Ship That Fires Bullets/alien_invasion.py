'''
ESTRUCTURA BASICA DE UN JUEGO ESCRITO EN PYGAME
'''
import sys
import pygame as pygame

def run_game():
    # Inicializamos el JUEGO y se crea un OBJETO VENTANA
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

  # LOOP PRINCIPAL DEL JUEGO
    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()
        
        pygame.display.flip()

# Ponemos en EJECUCION ell JUEGO
run_game()