sandwich_orders = ['mixto', 'bacon y queso', 'lomo y pimientos', 'tortilla patata', 'hamburguesa']
finished_sandwich = []

# La CONDICION 'WHILE LISTA[]' quiere decir que MIENTRAS EXISTAN ELEMENTOS en la LISTA[] se EJECUTARA el WHILE.
while sandwich_orders:
    # El METODO pop() ELIMINA y DEVUELVE el ULTIMO ELEMENTO de una LISTA.
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich + ' sandwitch')
    # AÑADIMOS el ELEMENTO EXTRAIDO a la NUEVA LISTA.
    finished_sandwich.append(current_sandwich)

print('\nList of Made Sandwitch:\n')
for sandwich in finished_sandwich:
    print('- ' + sandwich)

