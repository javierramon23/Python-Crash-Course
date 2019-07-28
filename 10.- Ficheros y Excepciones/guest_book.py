file_name = 'guest_book.txt'

guest_name = input('Hi, what is your name?: ')

# El BUCLE FINALIZA cuando el USUARIO NO META NADA y PULSE INTRO.
while guest_name != '':
    print('Welcome {}'.format(guest_name))
    
    with open(file_name, 'a') as file_object:
        # Si NO se AÑADE el SALTO DE LINEA al final el METODO ".write()" ESCRIBE A CONTINUACION
        # NO en una NUEVA LINEA.
        file_object.write(guest_name + ' login into the system\n')
    
    guest_name = input('Hi, what is your name?: ')