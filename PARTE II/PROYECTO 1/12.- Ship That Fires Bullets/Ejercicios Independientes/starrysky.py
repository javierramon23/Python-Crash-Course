import pygame
import sys
from star import Star
from pygame.sprite import Group

def number_stars():
    pass

def number_rows():
    pass

def create_star(screen, stars, star_number, row_number):
    star = Star(screen)
    star.rect.x = star.rect.width + 2 * star.rect.width * star_number
    star.rect.y =
    stars.add(star)

def create_constellation(screen, stars, number_stars, number_rows):


    for row_number in range(number_rows):
        for star_number in range(number_stars):
            create_star(screen, stars, star, row)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Starry Sky')

    stars = Group()
    create_constellation(screen, stars)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        screen.fill((255,255,250))
        stars.draw(screen)
        pygame.display.flip()

run_game()
    