precios = ['Gratis', '10$', '15$']

edad = input('Cuantos años tienes?: ')

while edad != 'quit':
    intEdad = int(edad)
    if intEdad < 3:
        print('El precio de tu entrada es: ' + precios[0])
    elif intEdad >= 3 and intEdad <= 12:
        print('El precio de tu entrada es: ' + precios[1])
    else:
        print('El precio de tu entrada es: ' + precios[2])
    
    edad = input('Cuantos años tienes?: ')