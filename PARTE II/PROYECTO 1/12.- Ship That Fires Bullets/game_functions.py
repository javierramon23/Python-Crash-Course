import sys
import pygame

def check_evets(ship):
    '''RESPUESTA a los EVENTOS del TECLADO y RATON'''
    # BUCLE que "ESCUCHA" los EVENTOS que se produzcan durante la ejecución del JUEGO
    for event in pygame.event.get():
        # Respuesta al EVENTO 'Quit'
        if event.type == pygame.QUIT:
            sys.exit()
        # Respuesta a la PULSACION del CURSOR DERECHO
        elif event.type == pygame.KEYDOWN:
            # Si la TECLA es el CURSOR DERECHO
            if event.key == pygame.K_RIGHT:
                # SE DESPLAZA LA IMAGEN(SUPERFICIE/RECT) A LA DERECHA
                # SE ACCEDE AL ATRIBUTO 'rect' DEFINIDO EN LA CLASE
                ship.rect.centerx += 5

def update_screen(ai_settings, screen, ship):
    '''ACTUALIZA/REFRESACA la "NUEVA VENTANA" CREADA DESPUES DE POSIBLES "EVENTOS"'''
    # Se 'RELLENA' la ventana con COLOR.
    screen.fill(ai_settings.bg_color)
    # DIBUJAMOS la NAVE.
    ship.blitme()
    # Se ACTUALIZA/REFRESCA la VENTANA del juego.
    pygame.display.flip() 