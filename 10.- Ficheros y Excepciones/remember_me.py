import json

def get_stored_username():
    '''
    CARGA EL NOMBRE DEL USUARIO DESDE UN FICHERO JSON
    '''
    file_name = 'username.json'
    try:
        with open(file_name) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        # SI el FICHERO NO EXISTE DEVUELVE la CONSTANTE Python "None"
        return None
    else:
        return username

def get_new_username():
    '''
    SOLICITA NOMBRE DE USUARIO y lo GUARDA.
    '''
    username = input('What is your name: ')
    file_name = 'username.json'
    with open(file_name, 'w') as file_obj:
        json.dump(username, file_obj)
    # Una vez se ha GUARDADO el NOMBRE DEL USUARIO, TB SE DEVUELVE.
    return username

def greet_user():
    username = get_stored_username()

    if username:
        print('Wellcome back, {}!'.format(username))
    else:
        username = get_new_username()
        print("We'll remember you when you come back, {}!".format(username))

greet_user()