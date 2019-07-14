'''
# Si se utiliza TRUE como CONDICION de SALIDA de un WHILE
# se esta creano un BUCLE INFINITO qeu finalizarmos con 'break'
while True:
    topping = input('Elige los topping para tu pizza: ')
    # COMPARACION de CADENAS.
    if topping == 'quit':
        # SALIMOS del WHILE.
        break
    print('Has elegido añadir ' + topping + ' a tu pizza.')
'''
'''
    OTRA FORMA DE IMPLEMENTAR EL WHILE
'''
# Se UTILIZA la CADENA introducida por el usuario como CONDICION de SALIDA
topping = input('Elige los topping para tu pizza: ')

# MIENTRAS no se introduza 'quit'
while topping != 'quit':
    # Se MUESTRA el topping
    print('Has elegido añadir ' + topping + ' a tu pizza.')
    # Volvemos a preguntar para MODIFICAR la CONDICION de SALIDA
    topping = input('Elige los topping para tu pizza: ')


