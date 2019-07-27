class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can edit post']

    def show_privileges(self):
        print('Permisos del Usuario:')
        for privilege in self.privileges:
            print('- {}'.format(privilege))