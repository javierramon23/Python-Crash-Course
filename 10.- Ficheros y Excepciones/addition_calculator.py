# BUCLE INFINITO.
# FInalizaremos utilizando la SENTENCIA "break"
while True:
    # Solicitamos operandos de la operación.
    '''
    PARA TERMINAR el BUCLE INFINITO WHILE se establece una CONDICION
    sobre el PRIMER OPERANDO.
    '''
    operando_uno = input('Primer Operando: ')
    
    if operando_uno == 'q':
        '''
        La SENTENCIA "break" TERMINA CON EL BUCLE "MAS CERCANO" en el que ESTE.
        '''
        break

    operando_dos = input('Segundo Operando: ')

    # DENTRO del "try" se localiza el CODIGO que puede GENERAR UN ERROR/EXCEPCION.
    try:
        resultado = int(operando_uno) + int(operando_dos)
    # DENTRO del "except" se localiza el CODIGO que se EJECUTA CUANDO SE PRODUCE UN ERROR/EXCEPCION.
    except:
        print('Opss!, se ha producido un error al intentar realizar la operacion.\nPor favor, vuelva a intentarlo.')
    # DENTRO de la sentencia "else" se localiza el CODIGO que se EJECUTA CUANDO MO SE PRODUCE UN ERROR/EXCEPCION.
    else:
        print('El resultado de sumar {} y {} es: {}'.format(operando_uno, operando_dos, resultado))