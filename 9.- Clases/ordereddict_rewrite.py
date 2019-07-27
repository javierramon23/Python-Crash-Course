from collections import OrderedDict

def show_dictionary(diccionario):
    for key, value in diccionario.items():
        print('Clave: {} - Valor: {}'.format(key, value))

diccionario_normal = {}
diccionario_ordenado = OrderedDict()

diccionario_normal['key_1'] = 1
diccionario_normal['key_2'] = 2
diccionario_normal['key_3'] = 3
diccionario_normal['key_4'] = 4
diccionario_normal['key_5'] = 5
print(diccionario_normal)
show_dictionary(diccionario_normal)

diccionario_ordenado['key_1'] = 2
diccionario_ordenado['key_2'] = 4
diccionario_ordenado['key_3'] = 6
diccionario_ordenado['key_4'] = 8
diccionario_ordenado['key_5'] = 10
print(diccionario_ordenado)
show_dictionary(diccionario_ordenado)
