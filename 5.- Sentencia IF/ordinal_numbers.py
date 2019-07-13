numbers = list(range(1,10))

for number in numbers:
    if number == 1 :
        print('{}st'.format(number))
    elif number == 2:
        print('{}nd'.format(number))
    elif number == 3:
        print('{}rd'.format(number))
    else:
        print('{}th'.format(number))