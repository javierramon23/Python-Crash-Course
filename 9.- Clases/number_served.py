class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Es posible DEFINIR ATRIBUTOS X DEFECTO
        self.number_served = 0
    
    def describe_restaurant(self):
        print('El nombre del Restaurante es: {}'.format(self.restaurant_name))
        print('Preparan un tipo de cocina {}'.format(self.cuisine_type))
    
    def open_restaurant(self):
        print('Bienvenidos, el restaurante esta ABIERTO')
    
    # METODO SET para CAMBIAR el VALOR del ATRIBUTO
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant('La Torre', 'Tradicional')
print('El numero de clientes en este momento es de: {}'.format(restaurant.number_served))

# PODEMOS CAMBIAR el VALOR de un ATRIBUTO DIRECTAMENTE ACCEDIENDO a este PERO NO SE RECOMIENDA
# ES MEJOR CREAR UNA SERIE DE METODOS GET/SET para TRABAJAR con los ATRIBUTOS de FORMA "INDIRECTA"
restaurant.number_served = 10
print('El numero de clientes en este momento es de: {}'.format(restaurant.number_served))

# METODO SET para el ATRIBUTO
restaurant.set_number_served(5)
print('El numero de clientes en este momento es de: {}'.format(restaurant.number_served))

restaurant.increment_number_served(10)
print('El numero de clientes en este momento es de: {}'.format(restaurant.number_served))