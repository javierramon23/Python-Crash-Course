# Cuando se utilizan los DOS ASTERISCOS en un PARAMETRO de la FUNCION
# PODEMOS PASAR un CONJUNTO de PARES CLAVE/VALOR a la FUNCION.
def build_profile(first, last, **user_info):
    # Se CREA un DICCIONARIO VACIO.
    profile = {}
    # Se INTRODUCEN los ARGUMENTOS 'FIJOS' en el DICCIONARIO
    profile['first_name'] = first
    profile['last_name'] = last
    # Se INTRODUCEN la LISTA de PARES CLAVE/VALOR al DICCIONARIO
    for key, value in user_info.items():
        # Se CREA un ENTRADA en el DICCIONARIO para cada PAR
        profile[key] = value
    # Se DEVUELVE el DICCIONARIO GENERADO.
    return profile

user_profile = build_profile('Javier', 'Ramon', edad=41, altura=1.74)
print(user_profile)