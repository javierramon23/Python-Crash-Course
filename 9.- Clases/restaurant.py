class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('El nombre del Restaurante es: {}'.format(self.restaurant_name))
        print('Preparan un tipo de cocina {}'.format(self.cuisine_type))
    
    def open_restaurant(self):
        print('Bienvenidos, el restaurante esta ABIERTO')

restaurant = Restaurant('La Menta', 'Tradicional')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()