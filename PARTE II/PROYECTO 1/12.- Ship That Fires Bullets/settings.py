class Settings():
    def __init__(self):
        '''INICIALIZA LAS PROPIEDADES DEL JUEGO'''
        # PROPIEDADES de la PANTALLA
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # PROPIEDADES DE LA NAVA
        self.ship_speed_factor = 10

        # PROPIEDADES DE LA MUNICION
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3