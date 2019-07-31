'''
CUENTA EL NUMERO DE VECES QUE APARECE UNA PALABRA EN UN TEXTO.
'''
def buscar_palabra(fichero_texto, palabra):
    # Se CONTROLA 
    try:
        # Se ABRE EL FICHERO PARA LECTURA
        with open(fichero_texto) as file_object:
            # Se LEE el FICHERO
            # El METODO "read()" LEE el FICHERO COMPLETO y la DEVUELVE COMO UN STRING.
            contenido = file_object.read()
    # Se CONTROLA la EXCEPCION del que el FICHERO no EXISTA.
    except FileNotFoundError:
        print('El FICHERO especificado no existe!.')
    else:
        # EL METODO "lower()" TRANSFORMA EL TEXTO a MINUSCULAS.
        # El METODO "count()" CUENTA EL NUMERO DE VECES QUE APARECE UNA PALABRA EN UN TEXTO.
        print(contenido.lower().count(palabra))


palabra = 'un'
fichero_texto = 'don_quijote.txt'

buscar_palabra(fichero_texto, palabra)
