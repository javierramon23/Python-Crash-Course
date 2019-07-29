number_one = input('Introduce el primer operando: ')
number_two = input('Introduce el segundo operando: ')

try:
    result = int(number_one) + int(number_two)
except ValueError:
    print('Opps, ha surgido algun problema con los operandos.')
else:
    print('El resultado de sumar {} + {} es: {}'.format(number_one, number_two, result))
