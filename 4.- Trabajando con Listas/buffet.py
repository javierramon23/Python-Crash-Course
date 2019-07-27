'''
    El NUMERO RECOMENDADO de CARACTERES para una LINEA de CODIGO PYTHON es 80!!!
'''

simple_foods = ('pasta', 'pizza', 'fries', 'fish and chips', 'rice')

print('Today Buffet:')
for food in simple_foods:
    print('- {}'.format(food))

# Las TUPLAS son INMUTABLES por lo que NO ES POSIBLE MODIFICARLAS.
# Cualquiera de los dos intentos que aparecen a continuación generarán un ERROR de COMPILACION
# simple_foods[0] = 'fresh fruit'
# simple_foods.append('fresh fruit')

# Para poder 'MODIFICAR' una TUPLA es necesario REESCRIBIRLA/SOBREESCRIBIRLA con las MODIFICACIONES.
simple_foods = ('fresh fruit', 'pizza', 'fried chiken', 'fish and chips', 'rice')

print('')

print('Today New Buffet:')
for food in simple_foods:
    print('- {}'.format(food))
