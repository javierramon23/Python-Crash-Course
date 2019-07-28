file_name = 'learning_python.txt'

'''
    Cuando se UTILIZA la SENTENCIA "with" para ABRIR un FICHERO
    nos AHORRAMOS tener que CERRAR el FICHERO cuando hemos terminado
    de trabajar con el.
'''
with open(file_name) as fichero_origen:
    # Con el METODO "read()" se LEE el FICHERO COMPLETO y se GUARDA en la VARIABLE
    '''
    IMPORTANTE:
    El METODO "read()" DEVUELVE un STRING VACIO(linea en blanco) cuando ALCANZA EL FINAL DEL FICHERO.
    '''
    contenido = fichero_origen.read()
    # print(contenido)
    # Para ELIMINAR la LINEA en BLANCO de FINAL de FICHERO podemos utilizar el METODO ".rstrip()"
    # que ELIMINA CUALQUIER ESPACIO en BLANCO que exista a la DERECHA de la CADENA que lo INVOCA.
    print(contenido.rstrip())

print('')

with open(file_name) as fichero_origen:
    # Tambien podemos utilizar un BUCLE "FOR" para LEER el FICHERO LINEA x LINEA
    for line in fichero_origen:
        '''
        IMPORTANTE:
        EN UN FICHERO, AL FINAL DE CADA LINEA QUE LO COMPONE EXISTE UN CARACTER DE SALTO DE LINEA(\n)
        QUE NO AFECTA CUANDO LEEMOS EL FICHERO COMPLTO PERO QUE SI SE MUESTRA CUANDO SE UTILIZA ESTA
        FORMA de LECTURA
        '''
        # print(line)
        # El METODO ".rstrip()" permite CORREGIR esta situacion.
        print(line.rstrip())

print('')

with open(file_name) as fichero_origen:
    # Con el METODO ".readlines()" se CREA una LISTA con CADA UNA de las LINEAS del FICHERO
    # OJO, TODAS LAS LINEAS TERMINA CON UN CARACTER DE SALTO(\n) QUE TB SE ALMACENA
    lines_list = fichero_origen.readlines()
    # print(lines_list)

for line in lines_list:
    print(line.rstrip())

'''
    CUANDO SE TRABAJA CON "with" PARA ABRIR FICHEROS, ESTE, DEVUELVE UN OBJETO
    CON EL CONTENIDO DEL FICHERO. ESTE OBJETO SOLO ESTA DISPONIBLE DENTRO DEL BLOQUE
    CREADO POR EL "with".

    PAR UTILIZARLO FUERA SE DEBE ASIGNAR SU CONTENIDO a OTRA VARIABLE.
'''
