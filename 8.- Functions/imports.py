# 1- Se IMPORTAN TODAS LAS FUNCIONES del MODULO
import my_functions

# 2- Se IMPORTA SOLO UNA FUNCION del MODULO
from my_functions import my_function

# 3- Se IMPORTA SOLO UNA FUNCION del MODULO y se le ASIGNA un AlIAS a esa FUNCION
from my_functions import my_function as mi_funcion

# 4- Se IMPORTAN TODAS las FUNCIONES del MODULO y se le ASIGNA un ALIAS al MODULO
import my_functions as mis_funciones

'''
    ESTA FORMA DE IMPORTAR MODULOS NO ESTA RECOMENDADA.

    5- Se IMPORTAN TODAS las FUNCIONES del MODULO para INVOCARLAS DIRECTAMENTE SIN UTILIZAR:
    la SINTAXIS: "nombre_modulo.nombre_funcion"
    
    from my_functions import *
'''

# Se utiliza la FUNCION IMPORTADA de la FORMA 1:
my_functions.my_function('Hola')
# Se utiliza la FUNCION IMPORTADA de la FORMA 2:
my_function('Hola')
# Se utiliza la FUNCION IMPORTADA de la FORMA 3:
mi_funcion('Hola')
# Se utiliza la FUNCION IMPORTADA de la FORMA 4:
mis_funciones.my_function('Hola')
# Se utiliza la FUNCION IMPORTADA de la FORMA 5:
# ESTA FORMA NO SE RECOMIENDA!!!!!.


