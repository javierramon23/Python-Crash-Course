'''
    5 ERRORES COMUNES DE UN PRINCIPIANTE PYTHON:
'''

'''
    1.- CREAR una COPIA de un DICCIONARIO o una LISTA:

    Para CREAR la COPIA de una LISTA o un DICCIONARIO NO SE PUEDE UTILIZAR
    el OPERADOR de ASIGNACION(=) DEBEMOS UTILIZAR el METODO copy().

    Para una LISTA TAMBIEN puede usarse la SINTAXIX: nombre_lista_a_copiar[:]
'''
lista_1 = [1, 2,3 ,4, 5]

diccionario_1 = {
        'clave_1': 'valor_1',
        'clave_2': 'valor_2',
        'clave_3': 'valor_3',
    }

# NO ES UNA COPIA, las DOS VARIABLES APUNTAN AL MISMO DICCIONARIO.
diccionario_2 = diccionario_1
# PARA LISTAS.
lista_2 = lista_1

# ESTA ES LA FORMA CORRECTA.
diccionario_2 = diccionario_1.copy()
# PARA LISTAS TAMBIEN SIRVE.
lista_2 = lista_1[:]

'''
    2.- UTILIZAR BOOLEANOS COMO CLAVES EN DICCIONARIOS:

    OJO cuando se UTILIZAN CLAVES de TIPO BOOLEANO a un DICCIONARIO ya que:
        - El valor True = 1
        - El valor False = 0
    
    Por lo que si se COMBINA el uso de ENTEROS y BOOLEANOS:
        
        nombre_diccionario[0] = nombre_diccionario[False]
        nombre_diccionadio[1] = nombre_diccionario[True]
    
    Y los VALORES asignados a esas CLAVES se SOBREESCRIBIRAN.
'''

# Estas 4 EXPRESIONES son EQUIVALENTES POR LO QUE los VALORES 'valor_0' y 'valor_1',
# se SOBREESCRIBIRIAN por 'nuevo_valor_0' y 'nuevo_valor_1'
diccionario = {}

diccionario[0] = 'valor_0'
diccionario[1] = 'valor_1'

diccionario[True] = 'nuevo_valor_0'
diccionario[False] = 'nuevo_valor_1'

'''
    3.- ACTUALIZAR LISTA y DICCIONARIOS:

    NO SE DEBE ASIGNAR LA SALIDA DE UN METODO COMO sort(), update(), append(), etc
    a una VARIABLE puesto que el RESULTADO NO VA A SER EL DESEADO.

    NO DEMEMOS utilizar la SINTAXIS:

        1.- AÑADIR un ELEMENTO a una LISTA:
            lista = [lista_elementos]
            lista = lista.append(nuevo_elemento)
        
        2.- AÑADIR un ELEMENTO a un DICCIONARIO:
            diccionario = {elementos_diccionario}
            diccionario = diccionario.update({nuevo_par_clave_valor})
        
        3.- ORDENAR una LISTA:
            lista = [lista_elementos]
            lista = lista.sort(lista_elementos)
    
    ESTOS CODIGOS NO VAN A FUNCIONAR COMO SE ESPERA.
    Esta clase de METODOS DEBEN EJECUTARSE SIN ASIGNARLOS a NADA:

        - lista.append(nuevo_elemento)
        - diccionario.update({nuevo_elemento_diccionario})
        - lista.sort(lista_elementos)

'''

'''
    4.- STRING INTERNING, OPERADOR '==' y OPERADOR 'is':

        OJO CON el STRING INTERNING:
            - La forma en que PYTHON TRABAJA DE FORMA INTERNA CON STRINGS:
              https://dev.to/anuragrana/5-common-mistakes-made-by-beginner-python-programmers-5ggp

        RECORDAR TAMBIEN que el OPERADOR '=' es DIFERENTE que el OPERADOR 'is':
            - El OPERADOR '==' comprueba si los VALORES SON IGUALES O NO.
            - El OPERADOR 'is' comprueba se las DOS VARIABLES APUNTAN al MISMO OBJETO.
'''

'''
    5.- Los ARGUMENTOS POR DEFECTO de una FUNCION SE EVALUAN SOLO la PRIMERA VEZ
    QUE SE INVOCA LA FUNCION, las veces SIGUIENTES tendran el VALOR que tenian
    cuando FINALIZO la EJECUCIÓN de la FUNCION.
'''

def funcion(a, lista = []):
    lista.append(a)
    return lista

# Cuando se INVOCA la PRIMERA VEZ
print('Cuando se invoca la FUNCION la PRIMERA VEZ: {}'.format(funcion(1)))
# DEVUELVE LA LISTA ESPERADA: [1]

# PERO la SEGUNDA VEZ
print('Cuando se invoca la FUNCION la SEGUNDA VEZ: {}'.format(funcion(2)))
# EL RESULTADO ESPERADO SERIA la LISTA: [2]
# PERO el RESULTADO es la LISTA: [1,2]

'''
    ERROR EXTRA: ¡¡¡NO MEZCLAR EL USO DE ESPACIOS EN BLANCO CON EL DE TABULADORES!!!
'''