glossary = {
        'variable': 'es un nombre que se refiere a un objeto en memoria.',
        'constante': 'es un tipo de variable que no puede ser cambiada.',
        'booleano': 'es un tipo de dato que solo puede tener dos valores: verdadero o falso.',
        'lista': 'son variables que almecenan arrays.',
        'tupla': 'es un tipo especial de lista ya que no puede modificarse.',
    }

print('Version 1.0:')
for word in glossary.items():
    print('- {}:\n\t{}'.format(word[0].title(), word[1].capitalize()))

print('\nVersion 2.0:')
'''
    Podemos DEFINIR una PAREJA de VARIABLES en el FOR para GUARDAR
    cada uno de los VALORES del PAR CLAVE/VALOR de un DICCIONARIO

    En lugar de tener que trabajar DIRECTAMENTE con la TUPLA que 
    DEVUELVE 'nombre_diccionario.items()'
'''
for word, definition in glossary.items():
    print('- {}:\n\t{}'.format(word.title(), definition.capitalize()))

# Otra forma de RECORRER un DICCIONARIO
# for key in glossary.keys():
    # print('- {}:\n\t{}'.format(key.title(), glossary[key].capitalize()))