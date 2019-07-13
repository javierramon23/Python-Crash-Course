'''
    TEST CONDICIONAL: Cualquier EXPRESIÓN que puede EVALUARSE a VERDADERO o FALSO (True o False).

    TIPO DATOS BOOLEANO: True o False.

    OPERADOR de IGUALDAD: == , OPERADOR de DESIGUALDAD: !=

    Otros OPERADORES de COMPARACION: >, <, >=, <=

    Con los OPERANDOS 'and' y 'or' es POSIBLE realizar TEST CONDICIONALES MULTIPLES (Y/O).

    ¡¡¡IMPORTANTE!!!
    Con los OPERANDOS 'in' y 'not in' es POSIBLE comprobar si un valor EXISTE/NO EXISTE en una LISTA.
'''
print('Test Condicional con CADENAS:')

string = 'javier'
print('Si la CADENA es {}'.format(string))
print('Es la CADENA igual a javier?: {}'.format(string == 'javier'))
print('Es la CADENA distinta a javier?: {}'.format(string != 'javier'))

string = 'luis'
print('Si la CADENA es {}'.format(string))
print('Es la CADENA igual a luis?: {}'.format(string == 'luis'))
print('Es la CADENA distinta a luis?: {}'.format(string != 'luis'))

print('')

'''
    Los METODOS lower() y upper() permiten transformar una CADENA a minusculas y MAYUCULAS respectivamente.
'''
print('Test Condicional con CADENAS en formato NO CASE SENSITIVE:')
string = 'JaViEr'
print('Si la CADENA es {}'.format(string))
print('Es la CADENA igual a Javier?: {}'.format(string.lower() == 'javier'))
print('Es la CADENA distinta a Javier?: {}'.format(string.lower() != 'javier'))

print('')

print('Test Condicional con NUMEROS:')
number = 23
print('Si el NUMERO es {}'.format(number))
print('Es {} IGUAL a 10?: {}'.format(number, number == 10))
print('Es {} DISTINTO a 10?: {}'.format(number, number != 10))
print('Es {} MENOR a 10?: {}'.format(number, number < 10))
print('Es {} MENOR o IGUAL a 10?: {}'.format(number, number <= 10))
print('Es {} MAYOR o IGUAL a 10?: {}'.format(number, number >= 10))
print('Es {} MAYOR a 10?: {}'.format(number, number > 10))

print('')

print('Test Condicional MULTIPLE:')
number = 30
print('Si el NUMERO es {}'.format(number))
print('Es {} MENOR que 100 Y MAYOR que 10?: {}'.format(number, number < 100 and number > 10))
print('Es {} MENOR que 100 Y MAYOR que 50?: {}'.format(number, number < 100 and number > 50))
print('Es {} MENOR que 10 Y MAYOR que 20?: {}'.format(number, number < 10 and number > 20))
print('Es {} MENOR que 100 O MAYOR que 20?: {}'.format(number, number < 100 or number > 20))
print('Es {} MENOR que 40 O MAYOR que 50?: {}'.format(number, number < 40 or number > 50))

print('')

print('Test Condicional sobre LISTAS:')
my_list = [1, 2, 3, 4 , 5]
print('Si mi lISTA es {}'.format(my_list))
print('ESTA el numero 10 dentro de la LISTA?: {}'.format(10 in my_list))
print('ESTA el numero 2 dentro de la LISTA?: {}'.format(2 in my_list))
print('El numero 10 NO ESTA dentro de la LISTA?: {}'.format(10 not in my_list))
print('El numero 2 NO ESTA dentro de la LISTA?: {}'.format(2 not in my_list))