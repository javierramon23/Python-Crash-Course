# Utilizando el NOMBRE del FICHERO que CONTIENE las FUNCIONES
# PODEMOS IMPORTAR TODAS LAS FUNCIONES que contiene el FICHERO.
import printing_functions

# Para hacerlo MAS FACIL podemos utilizar un ALIAS en la SENTENCIA 'import'
import printing_functions as print 

modelos_pendientes = ['modelo 1', 'modelo 2', 'modelo 3', 'modelo 4']
modelos_finalizados = []

# Para INVOCAR las FUNCIONES IMPORTADAS, se utiliza el NOMBRE del FICHERO IMPORTADO
# seguido de un PUNTO(.) y a continuación el NOMBRE de la FUNCION DESEADA.
printing_functions.print_models(modelos_pendientes, modelos_finalizados)
printing_functions.show_completed_models(modelos_finalizados)

# Si hemos DEFINIDO un ALIAS, utilizamos el ALIAS seguido de un PUNTO(.) y el NOMBRE de la FUNCION.
print.print_models(modelos_pendientes, modelos_finalizados)
print.show_completed_models(modelos_finalizados)


