# DICCIONARIO VACIO para GUARDAR USUARIOS y sus RESPUESTAS.
users_awser = {}

# CONDICION BOOLEANA para FINALIZAR el WHILE
end_poll = False

# MIENTRAS end_poll SEA FALSO:
while not end_poll:
    # USUARIO introduce NOMBRE y DESTINO
    user_name = input('Como te llamas?:')
    location = input('A que sitio te gustaría viajar este verano?: ')
    # Se GUARDA en una NUEVA ENTRADA del DICCIONARIO
    users_awser[user_name] = location

    # ¿Se quiere CONTINUAR?:
    repeat = input('Otro usuario?(SI/NO): ').upper()
    if repeat == 'NO':
        # Se CAMBIA el BOOLEANO para FINALIZAR el BUCLE
        end_poll = True
        
print('Lista de RESPUESTAS a la CONSULTA:\n')
# Se IMPRMIME el DICCIONARIO con los USUARIOS y sus RESPUESTAS.
for user, location in users_awser.items():
    print('Nombre de Usuario: {} - Lugar de Destino: {}'.format(user, location))