favorite_numbers = {
        'javier': 23, 
        'luis': 32, 
        'david': 33, 
        'laura': 14, 
        'ester': 20,
        }

print('Version 1.0')
for person in favorite_numbers.items():
    print('El numero favorito de {} es el {}'.format(person[0].capitalize(), person[1]))

print('\nVersion 2.0')
'''
    Podemos DEFINIR una PAREJA de VARIABLES en el FOR para GUARDAR
    cada uno de los VALORES del PAR CLAVE/VALOR de un DICCIONARIO

    En lugar de tener que trabajar DIRECTAMENTE con la TUPLA que 
    DEVUELVE 'nombre_diccionario.items()'
'''
for name, age in favorite_numbers.items():
    print('El numero favorito de {} es el {}'.format(name.capitalize(), age))
