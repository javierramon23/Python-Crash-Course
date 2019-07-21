def city_country(city, country):
    return '"{}, {}"'.format(city.title(), country.title())

print(city_country('teruel', 'españa'))
print(city_country('nueva york', 'usa'))
print(city_country('moscu', 'rusia'))