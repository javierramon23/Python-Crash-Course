numbers = list(range(1, 26))

print(numbers)

# RECORDAR QUE SIEMPRE LA PRIMERA POSICION DE UNA LISTA ES 0.
print('Los 3 primeros elementos de la lista son: {}'.format(numbers[:3]))

central_element = int(len(numbers)/2)
print('Los 3 elementos centrales de la lista son: {}'.format(numbers[central_element - 1:central_element + 2]))

# Con los INDICES NEGATIVOS nos referimos a los ELEMENTOS DESDE el FINAL de la LISTA.
# Siendo '-1' el ULTIMO ELEMENTO, '-2', el PENULTIMO, '-3' el ANTEPENULTIMO y asi sucesivamente.
print('Los 3 elementos finales de la lista son: {}'.format(numbers[-3:]))