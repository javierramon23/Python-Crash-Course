# Se IMPORtAN los MODULO NECESARIOS.
import sys
import pygame
from ship import Ship

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
        """ BUCLE GESTOR DE EVENTOS """
        for event in pygame.event.get():
            # MANEJADOR EVENTO 'QUIT'
            if event.type == pygame.QUIT:
                sys.exit()
            # MANEJADOR EVENTO 'PULSAR TECLA'
            if event.type == pygame.KEYDOWN:
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

            # MANEJADOR EVENTO 'SOLTAR TECLA'
            if event.type == pygame.KEYUP:
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

