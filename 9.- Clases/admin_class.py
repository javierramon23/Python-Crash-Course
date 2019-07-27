class User():
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

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can edit post']

    def show_privileges(self):
        print('Permisos del Usuario:')
        for privilege in self.privileges:
            print('- {}'.format(privilege))

class Admin(User):
    def __init__(self, first_name, last_name, age, born):
        super().__init__(first_name, last_name, age, born)
        # Para INICIALIZAR el ATRIBUTO se CREA una INSTANCIA de Privileges
        self.privileges = Privileges()