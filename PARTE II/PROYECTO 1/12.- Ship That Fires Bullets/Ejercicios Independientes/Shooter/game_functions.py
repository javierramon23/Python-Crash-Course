import sys
import pygame
from ship import Ship
from bullet import Bullet

def fire_bullet(screen, ship, bullets):
    # Se LIMITA el NUMERO de BALAS que se pueden DISPARAR.
    if len(bullets) < 3:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)

def check_quit_key(event):
    if event.type == pygame.QUIT:
        sys.exit()

def check_key_down(screen, ship, bullets, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            ship.move_up = True
        elif event.key == pygame.K_DOWN:
            ship.move_down = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(screen, ship, bullets)

def check_key_up(screen, ship, bullets, event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            ship.move_up = False
        elif event.key == pygame.K_DOWN:
            ship.move_down = False
        elif event.key == pygame.K_SPACE:
            pass

def check_events(screen, ship, bullets):
    for event in pygame.event.get():
        check_quit_key(event)
        check_key_down(screen, ship, bullets, event)
        check_key_up(screen, ship, bullets, event)

def update_screen(screen, ship, bullets):
    '''
        Se RELLENA el FONDO de la PANTALLA
        Se 'DIBUJAN' la NAVE y las BALAS
        y se ACTUALIZA la PANTALLA para mostrar los cambios.
    '''
    #
    screen.fill((230, 230, 230))
    #
    ship.blit_me()
    for bullet in bullets.sprites():
        bullet.draw_me()
    #
    pygame.display.flip()

def update_bullets(screen_width, bullets):
    '''
        ACTUALIZAMOS la POSICION de las BALAS y las BORRAMOS cuando
        salgan de la pantalla.
    '''
    bullets.update()

    for bullet in bullets.copy():
        if bullet.bullet_rect.left >= screen_width:
            bullets.remove(bullet)
       

        