file_name = 'guest.txt'

name = input('What is your name: ')

'''
    PARAMETROS ESCRITURA FICHEROS:
    w: Si fichero NO EXISTE, lo CREA y ESCRIBE. Si EXISTE, SOBREESCRIBE contenido.
    a: Si fichero NO EXISTE, lo CREA y ESCRIBE. Si EXISTE, AÑADE A CONTINUACIÓN PERO EN LA MISMA LINEA.
'''
with open(file_name, 'w') as file_object:
    file_object.write(name)