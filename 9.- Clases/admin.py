from users import User
from privileges import Privileges

class Admin(User):

    def __init__(self, first_name, last_name, age, born):
        super().__init__(first_name, last_name, age, born)
        # Para INICIALIZAR el ATRIBUTO se CREA una INSTANCIA de Privileges
        self.privileges = Privileges()

    '''
    Este METODO ya NO ES NECESARIO, se ha EXPORTADO a la CLASE "Privileges"
    y se DEBE usar de OTRA FORMA.

    def show_privileges(self):
        print("Permisos para el Usuario: {} {}".format(self.first_name, self.last_name))
        for privilege in self.privileges:
            print('- {}'.format(privilege))
    '''
            
admin = Admin('Javier', 'Ramon', 41, 'Barcelona')

'''
admin.show_privileges()
'''
'''
AHORA para INVOCAR el METODO "show_privileges()" DEBEMOS hacerlo a través del OBJETO
al que PERTENECE(privileges) al que a su vez ACCEDEMOS a TRAVES de OTRO OBJETO(admin).
'''
admin.privileges.show_privileges()