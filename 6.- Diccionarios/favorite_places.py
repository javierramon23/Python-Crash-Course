favorite_places = {
        'javier':['new york', 'tokio', 'pekin'],
        'luis':['madrid', 'valencia'],
        'laura':['granada', 'teruel'],
        'alex':['teruel', 'zaragoza', 'valencia'],
    }

for name, places in favorite_places.items():
    print('Los lugares favoritos de {}:'.format(name.capitalize()))
    for place in places:
        print('- {}'.format(place.title()))
    print('')
