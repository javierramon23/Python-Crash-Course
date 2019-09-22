import sys
import pygame
from bullet import Bullet
from alien import Alien

def get_number_aliens_x(ai_settings, alien_width):
    '''
    CALCULAMOS EL NUMERO DE ALIENS QUE VAN A ENTRAR EN UNA FILA.
    '''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    '''
    CALCULAMOS LAS FILAS DE ALIENS QUE VAN A ENTRAR EN LA PANTALLA.
    '''
    available_space_y = (ai_settings.screen_height - ( 3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''
    Se crea un NUEVO Alien, se POSICIONA en su LUGAR(x,y) y se mete en el GRUPO.
    '''
    alien = Alien(ai_settings, screen)
    # Almacenamos ALTURA y ANCHURA del Alien para calcular su posición.
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # Posicionamos el Alien.
    # Para POSICIONAR una IMAGEN, POSICIONAMOS las coordenadas X,Y de se SUPERFICIE(rectangulo).
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien_height + 2 * alien_height * row_number
    # Incluimos el nuevo Alien al Grupo.
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    ''' CREA LA FLOTA DE ALIENS ENEMIGOS '''
    # Este Alien es para saber cual es el acho que tiene, no se necesita para nada mas.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)
    
    # Se CREAN TODAS LAS FILAS DE ALIENS
    for row_number in range(number_rows):
        # Se CREA UNA FILA DE ALIENS.
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def fire_bullet(ai_settings, screen, ship, bullets):
    # COMPROBAMOS EL LIMITE DE BALAS PERMITIDAS
    if len(bullets) < ai_settings.bullets_allowed:
            # SE CREA UNA BALA
            new_bullet = Bullet(ai_settings, screen, ship)
            # SE AÑADE LA BALA AL GRUPO
            bullets.add(new_bullet)

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
        fire_bullet(ai_settings, screen, ship, bullets)
    # Si la TECLA es la 'Q'   
    elif event.key == pygame.K_q:
        # Tambien SALIMOS del JUEGO.
        sys.exit()

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
            

def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''ACTUALIZA/REFRESACA la "NUEVA VENTANA" CREADA DESPUES DE POSIBLES "EVENTOS"'''
    # Se 'RELLENA' la ventana con COLOR.
    screen.fill(ai_settings.bg_color)

    """ PARA TODAS LAS BALAS DEL GRUPO """
    for bullet in bullets.sprites():
        # SE LLAMA AL METODO 'draw_bullet()' de CADA BALA DEL GRUPO.
        # PARA DIBUJAR CADA BALA(BUFFER)
        bullet.draw_bullet()

    # DIBUJAMOS la NAVE.
    ship.blitme()
    '''
        Cuando se ejecuta el METODO 'draw()' de un GRUPO,
        ES COMO HACER UN 'blit()' EN CADA UNO DE LOS MIEMBROS DEL GRUPO.
        Por eso PARA DIBUJAR TODOS LOS ALIENS EJECUTAMOS 'draw()'.
        NOTA: NO ES NECESARIOel METODO 'blit_me()' en la CLASE Alien.
    '''
    aliens.draw(screen)

    # Se ACTUALIZA/REFRESCA la TODA LA VENTANA del juego.
    pygame.display.flip() 

def update_bullets(bullets):
    # SE ACTUALIZA EL MOVIMIENTO DE LAS BALAS
    # 'update()' de un GRUPO, INVOCA el 'update()' DE CADA ELEMENTO DEL GRUPO.
    bullets.update()
    """
        Cuando la BALAS desaparezcan de PANTALA hay que 'ELIMINARLAS'
        para que no CONSUMAN RECURSOS y REALENTICEN el juego.
        NO SE DEBEN ELIMINAR ELEMENTOS DE UN GRUPO O UNA LISTA CON UN BUCLE FOR
        POR LO TANTO LO HACEMOS SOBRE UNA COPIA DEL GRUPO QUE NOS PERMITE HACERLO
    """
    for bullet in bullets.copy():
        # CUANDO LA PARTE INFERIOR DE LA BALA ALCANZA LA PARTE SUPERIOR DE LA PANTALLA
        # SE ELIMINA DEL GRUPO.
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)