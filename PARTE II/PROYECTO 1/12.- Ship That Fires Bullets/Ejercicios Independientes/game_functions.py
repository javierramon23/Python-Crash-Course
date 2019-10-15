def get_number_stars(screen, star):
    available_space = 500 - 2 * star.rect.width
    number_stars = int(available_space / (2 * star.rect.width))
    return number_stars

def get_number_rows(screen, star):
    available_space = 500 - 2 * star.rect.height
    number_rows = int(available_space / (2 * star.rect.width))
    return number_rows