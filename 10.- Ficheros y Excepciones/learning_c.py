'''
El METODO "replace()" permite CAMBIAR CUALQUIER PALABRA de un STRING x OTRA.
SINTAXIS: mi_cadena.replace('palabra_inicial', 'palabra_final')
'''

file_name = 'learning_python.txt'

with open(file_name) as file_object:
    file_lines = file_object.readlines()

for line in file_lines:
    # Para ELIMINAR el SALTO de LINEA utilizamos el SLICE de Python, [inicio:fin]
    # que permite SELECCIONAR PARTES de una CADENA, en este caso, seleccionamos
    # TODA la CEDAN MENOS el ULTIMO CARACTER

    # Después aplicamos el METODO ".replace()" para SUSTITUIR la PALABRA.
    print(line[:-1].replace('Python', 'Java'))
    