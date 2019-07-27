guest = ['michel jordan', 'steve jobs', 'bill gates', 'pau gasol']

print('Envio de Invitaciones Generadas:\n')
for person in guest:
    print('Hola, {}, me gustaría invitarte este fin de semana a una cena.'.format(person.title()))

print('\nInvitacion Rechazada: {}\n'.format(guest[2].title()))

guest[2] = 'sandra julián'

print('NUEVO Envio de Invitaciones Generadas:\n')
for person in guest:
    print('Hola, {}, me gustaría invitarte este fin de semana a una cena.'.format(person.title()))