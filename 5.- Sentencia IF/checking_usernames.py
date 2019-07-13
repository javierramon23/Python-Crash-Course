# SUPONEMOS que los usernames se almacenan en el sistema SIEMPRE en MINUSCULAS.
current_users = ['user', 'admin', 'javier', 'mj23', 'administrador']

new_users = ['Javier', 'JavieR', 'JAVIER', 'JAvier', 'JaViEr']

for user in current_users:
    user = user.lower()

for user in new_users:
    # SIEMPRE se COMPARA el nuevo username 'PASADO' a MINUSCULAS para
    # hacer la COMPARACION 'CASE INSENSITIVE', NO DIFERENCIA ENTRE MAYUSCULAS y MINUSCULAS.
    # John = JOHN.
    if user.lower() in current_users:
        print('Sorry your username already exist, enter a new username.')
    else:
        print('Your username is available')