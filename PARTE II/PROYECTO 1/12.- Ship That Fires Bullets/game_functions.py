import sys
import pygame

def check_evets():
    '''RESPUESTA a los EVENTOS del TECLADO y RATON'''
    # BUCLE que "ESCUCHA" los EVENTOS que se produzcan durante la ejecución del JUEGO
    for event in pygame.event.get():
        # Respuesta al EVENTO 'Quit'
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    '''ACTUALIZA la IMAGENES de la VENTANA y "FLIP TO" la "NUEVA VENTANA"'''
    # Se 'RELLENA' la ventana con COLOR.
    screen.fill(ai_settings.bg_color)
    # DIBUJAMOS la NAVE.
    ship.blitme()
    # Se REFRESCA la VENTANA del juego.
    pygame.display.flip() 