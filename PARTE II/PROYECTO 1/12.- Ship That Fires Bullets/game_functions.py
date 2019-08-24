import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ CONTROLA LOS EVENTOS QUE SUCEDEN AL PULSAR UNA TECLA """
    # Si la TECLA es el CURSOR DERECHO
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Si la TECLA es el CURSOR IZQUIERDO
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # Si la TECLA es la BARRA ESPACIADORA
    elif event.key == pygame.K_SPACE:
        # SE CREA UNA BALA
        new_bullet = Bullet(ai_settings, screen, ship)
        # SE AÑADE LA BALA AL GRUPO
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """ CONTROLA LOS EVENTOS QUE SUCEDEN AL SOLTAR UNA TECLA """
    # Si la TECLA es el CURSOR DERECHO
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # Si la TECLA es el CURSOR DERECHO
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_evets(ai_settings, screen, ship, bullets):
    '''RESPUESTA a los EVENTOS del TECLADO y RATON'''
    # BUCLE que "ESCUCHA" los EVENTOS que se produzcan durante la ejecución del JUEGO
    for event in pygame.event.get():
        # Respuesta al EVENTO 'Quit'
        if event.type == pygame.QUIT:
            sys.exit()
        # Respuesta a la PULSACION de UNA TECLA
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # Respuesta a la NO PULSACION de UNA TECLA
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship, bullets):
    '''ACTUALIZA/REFRESACA la "NUEVA VENTANA" CREADA DESPUES DE POSIBLES "EVENTOS"'''
    # Se 'RELLENA' la ventana con COLOR.
    screen.fill(ai_settings.bg_color)
    """
    
    """
    for bullet in bullets.sprites():
        # SE LLAMA AL METODO 'draw_bullet()' de CADA BALA DEL GRUPO.
        # PARA DIBUJAR CADA BALA(BUFFER)
        bullet.draw_bullet()
    # DIBUJAMOS la NAVE.
    ship.blitme()
    # Se ACTUALIZA/REFRESCA la VENTANA del juego.
    pygame.display.flip() 