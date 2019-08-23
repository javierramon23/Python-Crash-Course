# Se IMPORtAN los MODULO NECESARIOS.
import sys
import pygame
from ship import Ship
import game_functions

def run_game():
    """ FUNCION PRINCIPAL QUE EJECUTA EL JUEGO """
    # INICIAMOS los COMPONENTES DE PYGAME.
    pygame.init()

    # DEFINIMOS UNA PANTALLA(VENTANA) PARA EL JUEGO y SU TAMAÑO
    # LO ASIGNAMOS A LA VARIABLE 'screen' PARA PODER TRABAJAR CON EL POSTERIORMENTE.
    screen = pygame.display.set_mode((250, 250))
    # COMO NO VAMOS A TRABAJAR POSTERIORMENTE CON EL NO ES NECESARIO ASIGNARLO.
    # ASIGNAMOS UN NOMBRE A LA PANTALLA(VENTANA) 
    pygame.display.set_caption('Rocket Game')

    # CREAMOS LA NAVE
    ship = Ship(screen)

    """ BUCLE PRINCIPAL DEL JUEGO """
    while True:
        """ MANEJADOR DE EVENTOS """  
        game_functions.manejador_eventos(ship)
        
        # SE ACTUALIZA EL MOVIMIENTO DE LA NAVE EN FUNCION DE COMO CAMBIEN LOS 'FLAGS'
        # EN EL GESTOR DE EVENTOS.
        ship.update_position()

        # RELLENAMOS LA PANTALLA DE COLOR
        screen.fill((230, 230, 230))

        # DIBUJAMOS LA NAVE EN LA PANTALLA (BUFFER)
        ship.blit_ship()

        # ACTUALIZAMOS LA PANTALLA(De BUFFER --> A PANTALLA)
        pygame.display.flip()

    
run_game()

