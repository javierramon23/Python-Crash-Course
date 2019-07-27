class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('El nombre del Restaurante es: {}'.format(self.restaurant_name))
        print('Preparan un tipo de cocina {}'.format(self.cuisine_type))
    
    def open_restaurant(self):
        print('Bienvenidos, el restaurante esta ABIERTO')

restaurant_1 = Restaurant('La Menta', 'Tradicional')
restaurant_2 = Restaurant('La Torre', 'Vanguardia')
restaurant_3 = Restaurant('El Milagro', 'Temporada')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()