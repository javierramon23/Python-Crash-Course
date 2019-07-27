# LISTA INICIA que NO DEBE ser MODIFICADA
magicians = ['mago1', 'mago2', 'mago3', 'mago4']


def make_great(lista):
    # LISTA AUXILIAR que almacena la LISTA MODIFICADA
    aux_magicians = []

    # INDICE para RECORRER la LISTA
    indice = 0
    
    while indice < len(lista):
        # Se AÑADE el NUEVO ELEMENTO a la NUEVA LISTA
        aux_magicians.append('The Great ' + lista[indice])
        indice += 1

    # DEVUELVE la LISTA MODIFICADA 
    return aux_magicians

def show_magicians(lista):
    for item in lista:
        print(item)

'''
    Para EVITAR MODIFICAR la LISTA INICIAL se PASA a la FUNCION
    una COPIA de la LISTA utilizando la SINTAXIS "nombre_lista[:]"
    De esta forma la LISTA no se ALTERA.
'''
new_magicians = make_great(magicians[:])
print('Lista de Magos Inicial:')
show_magicians(magicians)
print('')
print('Lista de Magos Modificada:')
show_magicians(new_magicians)
