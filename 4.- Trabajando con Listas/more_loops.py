my_foods = ['pizza', 'falafel', 'carrot cake','ice cream']
my_friends_foods = my_foods[:]

print('Mis comidas preferidas:')
for food in my_foods:
    print('- {}'.format(food))

print('')

print('Las comidas preferidas de mis amigos:')
for food in my_friends_foods:
    print('- {}'.format(food))