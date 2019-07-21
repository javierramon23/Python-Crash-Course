# DEFAULT ARGUMENTS
def make_shirt(size = 'l', text = 'i love python'):
    print('La Talla Seleccionada es: {}\nEl Mensaje elejido será: {}'.format(size.upper(), text.title()))

# Utilizara los DOS ARGUMENTOS x DEFECTO
make_shirt()
# Utilizara el SEGUNDO ARGUMENTO x DEFECTO
make_shirt('m')
# Utilizara el PRIMER ARGUMENTO x DEFECTO
# Para especificar el SEGUNDO ARGUMENTO se utiliza KEYWORD
make_shirt(text = 'i hate python')