# Se RECOMIENDA INDENTAR un DICCIONARIO para que sea mas CLARO de LEER.
# Se RECOMIENDA FINALIZAR un DICCIONARIO con una COMA FINAL(,)
person = {
        'first_name': 'javier', 
        'last_name': 'ramon', 
        'age': 41, 'city': 
        'teruel',
        }

print('Person Profile:')
print('---------------')
print('First Name: {}'.format(person['first_name'].capitalize()))
print('Last Name: {}'.format(person['last_name'].capitalize()))
print('Age: {}'.format(person['age']))
print('City: {}'.format(person['city'].capitalize()))

'''
    FORMAS DE RECORRER UN DICCIONARIO CON UN BUCLE FOR:
'''
# Recorre las CLAVES del DICCIONARIO.
for key in person.keys():
    print(person[key])
# Recorre los VALORES del DICCIONARIO.
for value in person.values():
    print(value)
# Recorre los ELEMENTOS(Clave/Valor) de un DICCIONARIO.
# Donde CADA ELEMENTO es una TUBLA de DOS VALORES, CLAVE y VALOR.
for key, value in person.items():
    print(value)
'''
    Podemos DEFINIR una PAREJA de VARIABLES en el FOR para GUARDAR
    cada uno de los VALORES del PAR CLAVE/VALOR de un DICCIONARIO

    En lugar de tener que trabajar DIRECTAMENTE con la TUPLA que 
    DEVUELVE 'nombre_diccionario.items()'
'''