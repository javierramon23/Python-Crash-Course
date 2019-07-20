def make_shirt(size, text):
    print('La talla elegida es: {}\nEl mensaje seleccionado es: {}'.format(size.capitalize(), text.title()))

# POSITIONAL ARGUMENTS
make_shirt('xl', 'keep calm Im a freak')

# KEYWORDS ARGUMENTS
# Permiten poner los ARGUMENTOS de la FUNCION en CUALQUIER ORDEN.
make_shirt(size = 'l', text = 'keep calm Im a stupid')
make_shirt(text = 'keep calm Im a stupid', size = 'l')