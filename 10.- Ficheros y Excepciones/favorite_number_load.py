# Se importa el MODULO "json"
import json

'''
FUNCION que ABRE un FICHERO y LEE un NUMERO
en FORMATO JSON para CARGARLO en el PROGRAMA.
'''
def load_number(file):
        try:
                with open(file_name) as file_obj:
                        number = json.load(file_obj)
        # Se CONTROLA la NO EXISTENCIA del FICHERO.
        except FileNotFoundError:
                print('El fichero solicitado no existe.')
        # Si NO SE PRODUCE ERROR 
        else:
                # Se DEVUELVE el NUMERO CARGADO.
                return(number)

file_name = 'favorite_number.json'

print('Tu numero favorito es es : {}'.format(load_number(file_name)))