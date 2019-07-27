# Cuando se utiliza el ASTERISCO en un PARAMETRO, Python CREA una TUPLA
# que CONTIENE TODOS LOS PARAMETROS PASADOS a la FUNCION cuando se LLAMA.
def your_ingredients(*ingredients):
    print('\nTUPLA creada por Python: {}'.format(ingredients))
    print('Summary of your Sandwitch Ingredients:')
    # Se RECORRE la TUPLA "ingredients" GENERADA por Python.
    for ingredient in ingredients:
        # IMPRIME el ingrediente.
        print('- {}'.format(ingredient.title()))

your_ingredients('jamon', 'queso')
your_ingredients('lomo', 'pimientos', 'cebolla')
your_ingredients('lechuga', 'tomate', 'cebolla', 'atun')





