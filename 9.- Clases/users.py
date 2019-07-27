class User:

    def __init__(self, first_name, last_name, age, born):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.born = born
    
    def describe_user(self):
        print('Nombre del Usuario: {} {}'.format(self.first_name, self.last_name))
        print('Edad del Usuario: {}'.format(self.age))
        print('Lugar de Nacimiento: {}'.format(self.born))

    def greet_user(self):
        print('Bienvenido {}, ahora estas registrado.'.format(self.first_name))

user_one = User('Javier', 'Ramon', 41, 'Barcelona')
user_two = User('Luis', 'Ramon', 31, 'Teruel')
user_three = User('Laura', 'Jambrina', 42, 'Teruel')

user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()

user_three.describe_user()
user_three.greet_user()