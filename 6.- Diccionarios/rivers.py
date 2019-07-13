rivers = {
        'nilo': 'egipto',
        'sena': 'francia',
        'mississipi': 'estados unidos',
        'amazonas': 'brasil',
        'ganges': 'india',
    }

print('Version 1.0')
for river in rivers.items():
    print('El {} corre a través de {}'.format(river[0].capitalize(), river[1].title()))

print('Version 2.0')
'''
    Podemos DEFINIR una PAREJA de VARIABLES en el FOR para GUARDAR
    cada uno de los VALORES del PAR CLAVE/VALOR de un DICCIONARIO

    En lugar de tener que trabajar DIRECTAMENTE con la TUPLA que 
    DEVUELVE 'nombre_diccionario.items()'
'''
for river, country in rivers.items():
    print('El {} corre a través de {}'.format(river.capitalize(), country.title()))

print('\nListado de los Rios:')
for river in rivers.keys():
    print(river.capitalize())

print('\nListado de Paises:')
for river in rivers.values():
    print(river.title())
