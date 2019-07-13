'''
    Stage of Life: Etapas de la Vida.
'''
# Se IMPORTA el MODULO 'random' para incluir las funciones que calculan
# numeroas aleatorios en Python.
import random

# El METODO 'randint(limite_inferior, limite_superior)' del 
# MODULO 'random' genera un NUMERO ENTERO ALEATORIO ENTRE
# 'limite_inferior' y 'limite superior.'
age = random.randint(1, 99)

print('If this person is {} years old, '.format(age))

'''
    La ESTRUCTURA if-elif-else está SOLO RECOMENDADA cuando SOLO ES NECESARIO
    TESTEAR UNA CONDICION, en este caso la EDAD(age).
'''
if age < 2:
    print('This person is a BABY.')
elif age >= 2 and age < 4:
     print('This person is a TODDLER.')
elif age >= 4 and age < 13:
     print('This person is a KID.')
elif age >= 13 and age < 20:
     print('This person is a TEENAGER.')
elif age >= 20 and age < 65:
     print('This person is an ADULT.')
else:
     print('This person is a ELDER.') 
