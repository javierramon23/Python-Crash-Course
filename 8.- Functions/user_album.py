def make_album(artist, album):
    return {
            'artist': artist,
            'album': album,
        }

# BUCLE INFINITO.
while True:
    # Se PIDE el PRIMER ARGUMENTO de la FUNCION.
    artist = input('Nombre del Cantante: ')
    # Sentencia que controla la REPETICION del WHILE
    if artist == 'quit':
        # 'ROMPEMOS' el BUCLE WHILE y SALIMOS.
        break
    # Se PIDE el SEGUNDO ARGUMENTO de la FUNCION.
    album = input('Titulo del Album: ')
    # Se INVOCA la FUNCION que CREA el DICCIONARIO y se IMPRIME el DICCIONARIO DEVUELTO.
    print(make_album(artist, album))