users_list = ['user', 'administrador', 'admin', 'boss', 'javier']

for user in users_list:
    if user == 'admin':
        print('Hello {}, would you like to see a status report?.'.format(user))
    else:
        print('Hello {}, thank you for logging in again.'.format(user))