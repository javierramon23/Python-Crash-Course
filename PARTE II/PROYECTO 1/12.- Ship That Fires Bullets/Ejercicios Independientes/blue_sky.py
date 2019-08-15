import sys
import pygame

def game_start():
    # SE INICIALIZAN TODOS LOS MODULOS NECESARIOS DE PYGAME
    pygame.init()
    
    # DEFINIMOS TAMAÑO Y TITULO DE LA VENTANA DE JUEGO.
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Blue Sky')

    """BUCLE PRINCIPAL DEL JUEGO"""
    while True:
        # CONTROLADOR de EVENTOS del JUEGO
        for event in pygame.event.get():
            # POSIBLES EVENTOS DEL JUEGO
            if event.type == pygame.QUIT:
                sys.exit()

        # COLOREAMOS VENTANA PRINCIPAL
        screen.fill((30, 195, 228))
        # ACTUALIZA/REFRESCA CONTENIDO VENTANA PRINCIPAL
        pygame.display.flip()

# INICIAMOS EL JUEGO
game_start()
