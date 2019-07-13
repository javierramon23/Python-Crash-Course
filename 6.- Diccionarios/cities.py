cities = {
        'teruel': {
                'country': 'Spain',
                'population': '30000',
                'fact': 'Small town in Spain',
            },
        'valencia': {
                'country': 'Spain',
                'population': '1000000',
                'fact': 'City of Fallas',
            },
        'madrid': {
                'country': 'Spain',
                'population': '5000000',
                'fact': 'Capital of country',
            },
    }

for city, info in cities.items():
    print('Información sobre la Ciudad de {}:'.format(city.capitalize()))
    for key, value in info.items():
        print('- {}: {}'.format(key.capitalize(), value))
    print('') 