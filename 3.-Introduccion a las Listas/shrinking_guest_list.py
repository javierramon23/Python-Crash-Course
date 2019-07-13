guest = ['michel jordan', 'steve jobs', 'bill gates', 'pau gasol']

print('Perdonar las molestias pero debido a causas externas solo quedan dos sitios libres para la cena:')

print('\tPerdona {}, pero al final no vas a poder asistir a la cena, lo siento.'.format(guest.pop()))
print('\tPerdona {}, pero al final no vas a poder asistir a la cena, lo siento.'.format(guest.pop()))

print()

print('Hola, {}, confirmarte que la cena se lelebrará el sabado a las 22:00, espero verte alli.'.format(guest[0]))
print('Hola, {}, confirmarte que la cena se lelebrará el sabado a las 22:00, espero verte alli.'.format(guest[1]))

del guest[1]
del guest[0]

print()

print('Contenido de la lista actual {} invitados: {}'.format(len(guest),guest))