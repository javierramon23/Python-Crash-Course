# Se IMPORTAN LAS LIBRERIAS NECESARIAS PARA LA APP.
import pygame                   # MODULO necesario para utilizar la LIBRERIA PYGAME.
import sys                      # MODULO necesario para utilizar 
from pygame.sprite import Group # MODULO necesario para utilizar SPRITES y sus variantes (GRUPOS).
import game_functions as gf     # MODULO PROPIO con las funciones necesarias para CREAR la constelacion.

"""
Funcion principal del juego.
"""
def run_game():
    # Se inician los modulos necesarios para ejecutar la libreria PYGAME.
    pygame.init()
    # Se define el tamaño de la PANTALLA/VENTANA del juego.
    screen = pygame.display.set_mode((500, 500))
    # Se define un NOMBRE para la PANTALLA/VENTANA del juego.
    # Se llama DIRECTAMENTE al METODO "set_caption" del ATRIBUTO "display"
    pygame.display.set_caption('Starry Sky')

    # Se crea un GRUPO(Modulo Sprite) para trabajar con varios OBJETOS de forma SIMULTANEA.
    stars = Group()

    # Se crea la constelación de estrellas.
    gf.create_constellation(screen, stars)

    """
    BUCLE PRINCIPAL del juego.
    BUCLE INFINITO.
    """
    while True:
        """
        BUCLE CONTROLADOR de EVENTOS.
        CAPTURA y RESPONDE a cada uno de los posibles EVENTOS que se producen durante
        la ejecución del juego.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        """
        ACTUALIZACION/REFRESCO de la PANTALLA/VENTANA del juego
        y de los OBJETOS que contiene.
        """
        screen.fill((255,255,250))
        stars.draw(screen)
        pygame.display.flip()

# Se llama a la funcion para que ponga en funcionamiento el juego.
run_game()
    