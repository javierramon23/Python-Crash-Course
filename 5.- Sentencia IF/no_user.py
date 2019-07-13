users_list = ['user', 'administrador', 'admin', 'boss', 'javier']

# Para comprobar si una LISTA esta VACIA debemos utilizar el siguiente
# TEST IF: 'if nombre_lista:', que DEVUELVE TRUE si CONTIENE ELEMENTOS
# y FALSE si NO LOS CONTIENE.
if users_list:
    for user in users_list:
        if user == 'admin':
            print('Hello {}, would you like to see a status report?.'.format(user))
        else:
            print('Hello {}, thank you for logging in again.'.format(user))
else:
    print('We need to find some users!')