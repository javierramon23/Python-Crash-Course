dog = {
        'kind': 'mammal',
        'name': 'dog'
    }

parrot = {
        'kind': 'bird',
        'name': 'parrot',
    }

shark = {
        'kind': 'fish',
        'name': 'shark',
    }

mamba = {
        'kind': 'reptile',
        'name': 'mamba',
    }

animals = [dog, parrot, mamba, shark]
print('')
print('List of Animals:')
print('---------------------------')
for animal in animals:
    for key, value in animal.items():
        print('{}:{}\t'.format(key.capitalize(), value.capitalize()), end = '')
    print('')
print('')       