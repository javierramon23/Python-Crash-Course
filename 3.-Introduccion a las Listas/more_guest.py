guest = ['michel jordan', 'steve jobs', 'bill gates', 'pau gasol']

print('Lista de Invitados:')

for person in guest:
    print('- {}'.format(person.title()))

guest.insert(0, 'alejandra julian')
guest.insert(int(len(guest)/2), 'david sancho')
guest.append('laura jambrina')

print('\nLista de Invitados (ACTULIZADA):')

for person in guest:
    print('- {}'.format(person.title()))

