def make_album(artist, album):
    # Podemos CREAR el DICCIONARIO 
    diccionario = {
            'artista': artist,
            'album': album,
        }
    
    # y LUEGO DEVOLVERLO.
    return diccionario

    '''
    Podemos DEVOLVER DIRECTAMENTE LA CREACION del DICCIONARIO.
    return {
            'artist': artist,
            'album': album,
        }
    '''

print(make_album('artista uno', 'album uno'))
print(make_album('artista dos', 'album dos'))
print(make_album('artista tres', 'album tres'))