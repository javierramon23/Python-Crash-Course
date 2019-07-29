def buscar_palabra(fichero_texto, palabra):
    try:
        with open(fichero_texto) as file_object:
            contenido = file_object.read()
    except FileNotFoundError:
        print()
    else:
        print(contenido.lower().count(palabra))

palabra = 'españa'
fichero_texto = 'la_regenta.txt'

buscar_palabra(fichero_texto, palabra)
