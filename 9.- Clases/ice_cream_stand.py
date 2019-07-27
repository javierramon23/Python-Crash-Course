# IMPORTAMOS la CLASE PADRE "Restaurant" desde el FICHERO "restaurant.py"
# para poder utilizarla.
from restaurant import Restaurant

'''
HERENCIA de CLASES
Cuando se DEFINE la CLASE HIJA, entre PARENTESIS se debe ESPECIFICAR el NOMBRE de la CLASE PADRE
de la que esta HEREDANDO.
'''
class IceCreamStand(Restaurant):
    '''
    CONSTRUCTOR de la CLASE HIJA
    La DEFINICION debe ESPECIFICAR TODOS los ARGUMENTOS NECESARIOS PARA "construir" la CLASE PADRE
    Ademas de los ATRIBUTOS PROPIOS de la NUEVA CLASE HIJA
    '''
    def __init__(self, restaurant_name, cuisine_type):
        # SE INVOCA al CONSTRUCTOR de la CLASE PADRE con los PARAMETROS NECESARIOS. 
        # Para hacerlo se utiliza la SINTAXIS: "super()." seguido del METODO __init__() del PADRE SIN el PARAMETRO "self"
        super().__init__(restaurant_name, cuisine_type)
        # Despues se AÑADEN los ATRIBUTOS PROPIOS de la CLASE HIJA.
        self.flavors = ['Chocolate', 'Vainilla', 'Fresa', 'Pistacho', 'Menta']

    def show_flavors(self):
        #print(self.flavors)
        for flavor in self.flavors:
            print('- {}'.format(flavor))

restaurant = IceCreamStand('La Heladeria', 'Reposteria')

print('Lista de Sabores de La Heladeria:')
restaurant.show_flavors()
