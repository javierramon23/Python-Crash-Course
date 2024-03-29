"""
ESTRUCTURA BASICA DE UN JUEGO ESCRITO EN PYGAME
"""
import pygame
# Se IMPORTA Settings para poder definir las Propiedades del JUEGO.
from settings import Settings
# Se IMPORTA Ship para poder utilizar la NAVE en el JUEGO.
from ship import Ship
# Se IMPORTA el MODULO de FUNCIONES del JUEGO.
import game_functions as gf
# Se IMPORTA Group para trabajar con CONJUNTOS de elementos (disparos, aliens, etc.)
from pygame.sprite import Group

'''
FUNCION que PONE en EJECUCION el JUEGO
'''
def run_game():
    '''
    Inicializamos el JUEGO y se crea un OBJETO VENTANA
    '''
    # pygame.init() pone en marcha los MODULOS necesarios para su funcionamiento.
    pygame.init()

    # Creamos INSTANCIA de la Clase Settings para poder UTILIZAR sus ATRIBUTOS en el juego.
    ai_settings = Settings()

    # TAMAÑO de la ventana del juego.
    screen = pygame.display.set_mode(
      (ai_settings.screen_width, ai_settings.screen_height))

    # 'NOMBRE' de la ventana del juego.
    pygame.display.set_caption('Alien Invasion')

    # INSTANCIAMOS un OBJETO SHIP
    ship = Ship(ai_settings, screen)
    
    # CREAMOS UN GRUPO(Sprite) para ALMACENAR las BALAS DISPARADAS y los ALIENS.
    bullets = Group()
    aliens  = Group()

    # CREAMOS la FLOTA DE ALIENS ENEMIGOS
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # LOOP PRINCIPAL DEL JUEGO
    while True:
      # ESCUCHAMOS LOS EVENTOS QUE SE PRODUZCAN en el JUEGO.
      gf.check_evets(ai_settings, screen, ship, bullets)
      # SE ACTUALIZA EL MOVIMIENTO DE LA NAVE
      ship.update()
      # SE ACTUALIZAN LAS BALAS
      gf.update_bullets(bullets)
      # ACTUALIZAMOS la VENTANA DEL JUEGO.
      gf.update_screen(ai_settings, screen, ship, aliens, bullets)

# Ponemos en EJECUCION el JUEGO
run_game()