favorite_numbers = {
        'javier': [9, 23,],
        'alex': [10,],
        'luis': [1, 3, 5, 7,],
        'laura': [2, 4, 6,],
        'sandra': [16, 21,],
    }

for name, numbers in favorite_numbers.items():
    print('Los Numeros Favoritos de {} son: '.format(name.capitalize()), end='')
    for number in numbers:
        print('{}, '.format(number), end='')
    print('')