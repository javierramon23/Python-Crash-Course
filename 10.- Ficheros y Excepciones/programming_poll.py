file_name = 'poll.txt'

awser = input('Hi, why o you like programming?:')

while awser != '':
    with open(file_name, 'a') as file_object:
        file_object.write(awser+'\n')
    awser = input('Hi, why o you like programming?:')