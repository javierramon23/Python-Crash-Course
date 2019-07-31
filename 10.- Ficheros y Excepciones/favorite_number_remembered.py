# Se IMPORTA el MODULO "json"
import json

'''
LA FUNCION INTENTA CARGAR UN NUMERO DESDE UN FICHERO JSON DADO.
SI EL NUMERO EXISTE, LO MUESTRA POR PANTALLA. SI NO EXISTE, SOLICITA
UNO Y LO GUARDA.
'''
def favorite_number(file_name):
    # CODIGO que puede causar una EXCEPCION.
    try:
        '''
        SI NO SE PRODUCE NINGUN ERROR, IMPLICA QUE YA EXISTE UN NUMERO,
        POR LO TANTO, SE LEE EL NUMERO CARGADO EN EL FICHERO y se DEVUELVE.
        '''
        with open(file_name) as file_obj:
            # Se CARGA el CONTENIDO del FICHERO JSON.
            number = json.load(file_obj)
           
    # Se CONTROLA LA NO EXISTENCIA del FICHERO.
    except FileNotFoundError:
        '''
        SI SE PRODUCE LA EXEPCION, ES QUE EL FICHERO NO EXISTE
        LO QUE SIGNIFICA QUE NO SE HA GUARDADO AUN NINGUN NUMERO,
        POR LO TANTO, SE PREGUNTA AL USUARIO Y SE GUARDA.
        '''
        number = input('Cual es tu numero favorito: ')
        with open(file_name, 'w') as file_obj:
            # Se ALMACENA el NUMERO INTRODUCIDO en el FICHERO JSON.
            json.dump(number, file_obj)
            print('Numero favorito guardado, me acordaré la proxima vez!!')

    # SI el FICHERO EXISTE (NO SE PRODUCE ERROR en el BLOQUE TRY)
    else:
        print('Tu numero favorito es el {}'.format(number))

favorite_number('favorite_number_remembered.json')

