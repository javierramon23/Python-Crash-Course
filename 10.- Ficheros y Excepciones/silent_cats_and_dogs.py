'''
COMO VAMOS A TRABAJAR CON VARIOS ARCHIVOS, EN LUGAR DE REPETIR CODIGO
VAMOS A CREAR UNA FUNCION Y LA INVOCAMOS PARA CADA ARCHIVO.
'''
def read_file(file_name):
    # CODIGO que puede GENERAR UNA EXCEPCION.
    try:
        with open(file_name) as file_object:
            content = file_object.read()
    # CAPTURAMOS la EXCEPCION QUE SE PRODUCIRA SI EL PROGRAMA NO ENCUENTRA EL FICHERO.
    except FileNotFoundError:
        # En este CASO NO VAMOS A REPORTAR EL ERROR, QUEREMOS QUE EL PROGRAMA SIMPLEMENTE CONTINUE.
        # Con la SENTENCIA "pass" le "decimos" a Python QUE NO HAGA NADA EN UN BLOQUE.
        pass
    else:
        # ELIMINAMOS LA LINEA EN BLANCO QUE APARECE AL LEER EL FICHERO.
        print(content.rstrip())

files = ['cats.txt', 'dogs.txt']

for file in files:
    read_file(file)