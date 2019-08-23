import sys
import pygame

def check_keydown_event(event, ship):
    """ POSIBLES EVENTOS AL PULSAR UNA TECLA """
    # TECLA PULSADA ES CURSOR ARRIBA
    if event.key == pygame.K_UP:
        ship.moving_up = True
    # TECLA PULSADA ES CURSOR ABAJO
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    # TECLA PULSADA ES CURSOR IZQUIERDA
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    # TECLA PULSADA ES CURSOR DERECHA
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

def check_keyup_event(event, ship):
    """ POSIBLES EVENTOS AL SOLTAR UNA TECLA """
    # TECLA SOLTADA ES CURSOR ARRIBA
    if event.key == pygame.K_UP:
        ship.moving_up = False
    # TECLA SOLTADA ES CURSOR ABAJO
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    # TECLA SOLTADA ES CURSOR IZQUIERDA
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    # TECLA SOLTADA ES CURSOR DERECHA
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

def manejador_eventos(ship):
    """ MANEJADOR DE EVENTOS """
    for event in pygame.event.get():
        # MANEJADOR EVENTO 'QUIT'
        if event.type == pygame.QUIT:
            sys.exit()
        # MANEJADOR EVENTO 'PULSAR TECLA'
        if event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        # MANEJADOR EVENTO 'SOLTAR TECLA'
        if event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

            