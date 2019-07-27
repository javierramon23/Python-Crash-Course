class User():

    def __init__(self, first_name, last_name, age, born):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.born = born
        self.login_attempts = 0
    
    def describe_user(self):
        print('Nombre del Usuario: {} {}'.format(self.first_name, self.last_name))
        print('Edad del Usuario: {}'.format(self.age))
        print('Lugar de Nacimiento: {}'.format(self.born))

    def greet_user(self):
        print('Bienvenido {}, ahora estas registrado.'.format(self.first_name))
    
    def get_login_attempts(self):
        return self.login_attempts
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
user = User('Javier', 'Ramon', 41, 'Barcelona')

while user.get_login_attempts() <= 3:
    print('Numero de intentos de acceso: {}'.format(user.get_login_attempts()))
    user.increment_login_attempts()

user.reset_login_attempts()
print('Acceso DENEGADO, espere antes de volver a acceder.')
print('Numero de intentos de acceso: {}'.format(user.get_login_attempts()))



