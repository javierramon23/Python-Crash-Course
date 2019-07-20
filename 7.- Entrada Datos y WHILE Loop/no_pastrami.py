sandwitch_order = ['pastrami', 'hamburguesa', 'mixto', 'pastrami', 'vegetal', 'tortilla', 'pastrami']

print('Lista de Bocadillos PENDIENTES:\n')

for sandwitch in sandwitch_order:
    print('-{}'.format(sandwitch))

print('\nPASTRAMI AGOTADO...\nActualizando LISTA de Bocadillos PENDIENTES...\n')

# MIENTRAS la CADENA BUSCADA se ENCUENTRE en la LISTA se REPITE el BUCLE.
while 'pastrami' in sandwitch_order:
    sandwitch_order.remove('pastrami')

for sandwitch in sandwitch_order:
    print('-{}'.format(sandwitch))