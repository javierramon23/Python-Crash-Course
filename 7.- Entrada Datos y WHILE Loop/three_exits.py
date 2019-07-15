# Test Condicional para salir del WHILE
print('EJERCICIO 1:')
ingrediente = input('Selecciona el ingrediente deseado: ')

while ingrediente != 'quit':
    print('Has seleccionado el siguiente ingrediente: ' + ingrediente.title())
    ingrediente = input('Selecciona el ingrediente deseado: ')

# Variable Activa para controlar las iteraciones del WHILE:
print('EJERCICIO 2:')
ingredientes_maximos = 4
numero_ingredientes = 1

while numero_ingredientes <= ingredientes_maximos:
    ingrediente = input('Selecciona el ingrediente deseado: ')
    print('Has seleccionado el siguiente ingrediente: ' + ingrediente.title())

    numero_ingredientes += 1

# Utilizar un BREAK para finalizar el WHILE:
print('EJERCICIO 3:')

while True:
    ingrediente = input('Selecciona el ingrediente deseado: ')

    if ingrediente == 'quit':
        break

    print('Has seleccionado el siguiente ingrediente: ' + ingrediente.title())

