magicians = ['mago1', 'mago2', 'mago3', 'mago4']

def show_magicians(lista):
    # Una vez nos pasan la LISTA la RECORREMOS para mostrar su contenido.
    for magician in lista:
        print('- {}'.format(magician.title()))

show_magicians(magicians)
