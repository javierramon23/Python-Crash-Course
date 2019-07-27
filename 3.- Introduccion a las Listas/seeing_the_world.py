places = ['Nueva York', 'Viena', 'Japon', 'Amazonas', 'Polo Norte']

print('Lista ORIGINAL:')
print(places)

# La FUNCION 'sorted()' devuelve la LISTA ORDENADA pero NO MODIFICA la LISTA ORIGEN.
print('Lista ORDENADA ALFABETICAMENTE de FORMA TEMPORAL:')
print(sorted(places))
print('Lista ORIGINAL:')
print(places)

# Si se añade el PARAMETRO 'reverse=True' devuelve la LISTA ORDENADA INVERSA pero NO MODIFICA la LISTA ORIGEN.
print('Lista ORDENADA ALFABETICAMENTE de FORMA INVERSA y TEMPORAL:')
print(sorted(places, reverse=True))
print('Lista ORIGINAL:')
print(places)

# El METODO reverse() INVIERTE EL ORDEN de los ELEMENTOS de una LISTA de FORMA PERMANENTE.
places.reverse()
print('Lista ORIGINAL de FORMA INVERSA:')
print(places)

places.reverse()
print('Lista ORIGINAL:')
print(places)

# El METODO sort() ORDENA ALFABETICAMENTE los ELEMENTOS de una LISTA de FORMA PERMANENTE.
places.sort()
print('Lista ORIGINAL ORDENADA ALFABETICAMENTE de FORMA PERMANENTE:')
print(places)

# Si se añade el PARAMETRO 'reverse=True' el ORDEN de los ELEMENTOS es INVERSO y PERMANENTE.
places.sort(reverse=True)
print('Lista ORIGINAL ORDENADA ALFABETICAMENTE de FORMA INVERSA y PERMANENTE:')
print(places)



