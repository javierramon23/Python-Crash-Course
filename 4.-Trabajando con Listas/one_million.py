# Se CREA una LISTA con los NUMEROS de 1 al 1vMillon
# con 'list()' podemos definir una lista SIN necesidad de hacerlo de forma EXPLICITA.
numbers = list(range(1,1000000))

for number in numbers:
    print(number, end=',')

print(number + 1)