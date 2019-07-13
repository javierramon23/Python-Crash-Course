# Se CREA una LISTA VACIA.
cubes = []

for number in range(1, 11):
    # Se AÑADE AL FINAL de la LISTA.
    # El OPERANDO '**' es la POTENCIA en PYTHON
    cubes.append(number ** 3)

for number in cubes:
    print(number)