def describe_city(city, country = 'España'):
    print('{} es una ciudad de {}.'.format(city, country))

describe_city('Teruel')
describe_city('Valencia')
describe_city('New York', country = 'EEUU')