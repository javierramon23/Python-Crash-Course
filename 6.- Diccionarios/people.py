person_1 = {
        'first': 'javier', 
        'last': 'ramon', 
        'age': '41', 
        'city': 'teruel',
        }

person_2 = {
        'first': 'laura', 
        'last': 'jambrina', 
        'age': '42', 
        'city': 'teruel',
        }

person_3 = {
        'first': 'alejandra', 
        'last': 'julian', 
        'age': '41', 
        'city': 'teruel',
        }

# Se crea una LISTA de DICCIONARIOS:
people_list = [person_1, person_2, person_3]

# Se RECORRE la LISTA:
for person in people_list:
    # Se RECORRE el DICCIONARIO:
    for tag, value in person.items():
        print('- {}:'.format(tag.capitalize()), end=' ')

        if value.isdigit():
            print('{}'.format(value))
        else:
            print('{}'.format(value.capitalize()))

    print('')