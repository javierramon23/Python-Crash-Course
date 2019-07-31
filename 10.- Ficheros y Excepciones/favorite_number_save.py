# Se importa el MODULO "json"
import json

'''
FUNCION que ABRE un FICHERO y GUARDA un NUMERO
en FORMATO JSON.
'''
def save_number(number, file):
        try:
                with open(file_name, 'w') as file_obj:
                        json.dump(number, file_obj)
        # Se CONTROLA la NO EXISTENCIA del FICHERO INDICADO                
        except FileNotFoundError:
                print('El fichero solicitado no existe.')

file_name = 'favorite_number.json'

favorite_number = input ('Cual es tu numero favorito?: ')

save_number(int(favorite_number), file_name)