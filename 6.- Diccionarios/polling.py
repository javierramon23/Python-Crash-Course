name_list = ['javier', 'jen', 'luis', 'sarah', 'alex', 'edward', 'laura', 'phil']

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

# RECORREMOS la LISTA de NOMBRES
for name in name_list:
    # Se COMPRUEBA que el NOMBRE de la LISTA EXISTA en el DICCIONARIO:
    # PODEMOS utilizar una SENTENCIA IF para BUSCAR  CLAVE en UN DICCIONARIO
    # IGUAL que se hace con una LISTA/TUPLA.
    if name in favorite_languages:
        print('{}, Gracias por participar en nuestra encuesta'.format(name.capitalize()))
    else:
        print('Hola, {}, me gustaría invitarte a que participaras en nuestra encuesta'.format(name.capitalize()))