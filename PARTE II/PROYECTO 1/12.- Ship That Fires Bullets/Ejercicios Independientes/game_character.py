import sys
import pygame

from character import Character

def game_start():
    pygame.init()
    
    # DEFINIMOS TAMAÑO Y TITULO DE LA VENTANA DE JUEGO.
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Blue Sky')
    
    # SE CREA UNA INSTANCIA DEL OBJETO 'Character'
    character = Character(screen)

    """BUCLE PRINCIPAL DEL JUEGO"""
    while True:
        # CONTROLADOR de EVENTOS del JUEGO
        for event in pygame.event.get():
            # POSIBLES EVENTOS DEL JUEGO
            if event.type == pygame.QUIT:
                sys.exit()

        # COLOREAMOS VENTANA PRINCIPAL
        screen.fill((255, 255, 255))
        # INSERTAMOS LA IMAGEN EN EL BUFFER DE LA VENTANA
        character.blit_me()
        # ACTUALIZA/REFRESCA CONTENIDO VENTANA PRINCIPAL
        pygame.display.flip()

game_start()