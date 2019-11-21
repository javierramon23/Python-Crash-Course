# Se IMPORTAN LAS LIBRERIAS/MODULOS NECESARIOS PARA LA .
from star import Star

def get_number_stars(screen, star):
    available_space = 500 - 2 * star.rect.width
    number_stars = int(available_space / (2 * star.rect.width))
    return number_stars

def get_number_rows(screen, star):
    available_space = 500 - 2 * star.rect.height
    number_rows = int(available_space / (2 * star.rect.width))
    return number_rows

def create_star(screen, stars, star_number, row_number):
    star = Star(screen)
    star.rect.x = star.rect.width + 2 * star.rect.width * star_number
    star.rect.y = star.rect.width + 2 * star.rect.height * row_number
    stars.add(star)

def create_constellation(screen, stars):
    star = Star(screen)
    star.width = star.rect.width

    number_stars = get_number_stars(screen, star)
    number_rows = get_number_rows(screen, star)

    for row_number in range(number_rows):
        for star_number in range(number_stars):
            create_star(screen, stars, star_number, row_number)