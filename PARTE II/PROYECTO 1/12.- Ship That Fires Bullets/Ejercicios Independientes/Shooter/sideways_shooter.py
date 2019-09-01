import pygame
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
import game_functions

def run_game():
    pygame.init()

    screen_hight = 500
    screen_width = 700
    
    #
    screen = pygame.display.set_mode((screen_width,screen_hight))
    pygame.display.set_caption('Sideways Shooter')
    
    #
    ship = Ship(screen)
    bullets = Group()

    while True:
        #
        game_functions.check_events(screen, ship, bullets)
        #
        ship.update()
        #
        game_functions.update_bullets(screen_width, bullets)
        #
        game_functions.update_screen(screen, ship, bullets)

run_game()