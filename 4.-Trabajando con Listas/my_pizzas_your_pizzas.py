my_pizzas = ['don topo', 'picarosa', 'serrana']

# Para hacer una COPIA de una LISTA utilizamos la NOTACION [:]
friends_pizzas = my_pizzas[:]

my_pizzas.append('barbacoa')
friends_pizzas.append('4 estaciones')

print('Mis Pizzas Favoritas son:')
for pizza in my_pizzas:
    print('- {}'.format(pizza))

print('')

print('Las Pizzas Favoritas de mis amigos son:')
for pizza in friends_pizzas:
    print('- {}'.format(pizza))