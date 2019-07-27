magicians = ['mago1', 'mago2', 'mago3', 'mago4']
aux_magicians = []

# def make_great(lista):
    # Para EDITAR los elementos de una LISTA, NO SE DEBE UTILIZAR
    # un BUCLE "FOR", la EDICION DEBE REALIZARSE con un BUCLE "WHILE"
    
    #for magician in lista:
        #pass
    
    #Una de las formas de poder hacerlo es con un INDICE y la LONGITUD de la LISTA
    #en un BUCLE WHILE

    #index = 0
    #while index < len(lista):
        #lista[index] = 'The Great ' + lista[index]
        #index += 1

'''
Otra forma es partiendo de la LISTA ORIGEN, utilizar una LISTA SECUNDARIA.
Extraer cdada elemento de una, MODIFICARLO, y INSERTARLO en la otra a través
de un BUCLE WHILE
'''
def other_make_great(lista_origen, lista_destino):
    while magicians:
        magician = magicians.pop()
        magician = 'The Great ' + magician
        aux_magicians.append(magician)

        
def show_magicians(lista):
    # Una vez nos pasan la LISTA la RECORREMOS para mostrar su contenido.
    for magician in lista:
        print('- {}'.format(magician.title()))

# Funcion con BUCLE FOR y un INDICE
# make_great(magicians)

# Funcion con BUCLE WHILE y LISTA AUXILIAR
# NOTAR que al utilizar esta FUNCION, el ORDEN de los ELEMENTOS se INVIERTE.
other_make_great(magicians, aux_magicians)

show_magicians(aux_magicians)