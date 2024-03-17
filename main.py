# Fabio Carrozza. C.I: 30714977. Proyecto: Metrotify

# Se importan las clases, funciones y librerías a usarse en el programa
import uuid
import matplotlib
from matplotlib import pyplot
import datetime
from funciones import download_users, download_songs, download_albums, download_playlists, get_artist_streams, get_likes, get_listener_likes
from funciones import get_id, get_listener_info, get_artist_info, get_usernames, get_names
from funciones import write_users, change_users_info, buscador, delete_user, streams_listener, reproducciones_cancion
from funciones import json_files, write_likes, get_likes_watch, delete_likes, write_songs
from funciones import get_my_songs, write_albums, write_playlists, top_5
from playlist import Playlist
from album import Album
from song import Song
from user import Listener, Musician

def main():
    """Esta es la función principal del programa. 
    En esta se cuidará la estética y la funcionalidad"""

    # Estas son las funciones para construir todos los objetos tomando en cuenta la API y los datos en el txt
    jsons = json_files()
    users_0 = download_users()
    songs = download_songs(users_0)
    albums = download_albums(users_0, songs)
    playlists = download_playlists(users_0, songs)
    users = get_artist_streams(users_0, songs)
    users = get_likes(users)
    users = get_listener_likes(users)
    songs = get_likes(songs)
    albums = get_likes(albums)
    playlists = get_likes(playlists)

    # Estas funciones son para facilitar la búsqueda de información
    users_id = get_id(users)
    songs_id = get_id(songs)
    albums_id = get_id(albums)
    playlists_id = get_id(playlists)
    all_usernames = get_usernames(users)
    songs_names = get_names(songs)
    albums_names = get_names(albums)
    playlists_names = get_names(playlists)

    # Esta es una variable de control que se usará durante todo el programa
    control = False
    control_0 = False

    # En esta variable se guardará el nombre del usuario que esté usando el programa
    username = None

    # En esta variable se guarda el objeto del usuario que está usando el programa
    usuario_activo = None

    while True:
        while username == None:
            control = False
            print("Bienvenido a Metrotify")
            print("""--> 1: Iniciar sesión
--> 2: Registrar nuevo usuario
--> 0: Salir del programa""")
            x = input("Opción: ")
            if x == "0":
                quit()
            if x == "1":
                while control != True:
                    control = False
                    y = input("Username: ")
                    for i in users:
                        if (i.username) == y:
                            username = y
                            usuario_activo = i
                            control = True
                            break

                    if username == None:            
                        print("Username no reconocido")
                        print("""--> 1: Regresar
--> 2: Seguir""")
                        z = input("Opción: ")
                        if z == "1":
                            control = True

            if x == "2":
                while control != True:
                    print("A continuación, registrará un nuevo usuario")
                    control = False
                    id_new_user = str(uuid.uuid4())
                    name_new_user = None
                    username_new_user = None
                    email_new_user = None
                    type_new_user = None
                    while name_new_user == None:
                        x = input("Nombre: ")
                        y = True
                        for i in x:
                            if i.isnumeric() == True:
                                y = False
                                print("El nombre no debe tener números")
                                break

                        if y == True:
                            name_new_user = x

                    while username_new_user == None: 
                        x = input("Username: ")
                        y = True
                        if x in all_usernames:
                            y = False
                            print("Ese usuario ya fue escogido")
                        if x not in all_usernames:
                            username_new_user = x
                    
                    while email_new_user == None: 
                        x = input("Email: ")
                        y = True
                        if "@" not in x:
                            y = False
                            print("Escriba un correo válido")
                        if "@" in x:
                            email_new_user = x

                    while type_new_user != "listener" and type_new_user != "musician":
                        print("Escoja si desea ser 'listener' o 'musician'")
                        type_new_user = input("Tipo de usuario: ")

                    if type_new_user == "listener":
                        new_user = Listener(id_new_user, name_new_user, email_new_user, username_new_user)
                        users.append(new_user)
                        username = new_user.username
                        usuario_activo = new_user
                        write_users(new_user)
                        control = True

                    if type_new_user == "musician":
                        new_user = Musician(id_new_user, name_new_user, email_new_user, username_new_user)
                        users.append(new_user)
                        username = new_user.username
                        usuario_activo = new_user
                        write_users(new_user)
                        control = True
        
        if username != None:
            if isinstance(usuario_activo, Listener) == True: 
                print(get_listener_info(users, username, albums, songs, playlists, albums_id, songs_id, playlists_id))
            
            if isinstance(usuario_activo, Musician) == True:
                get_artist_info(users, username, albums, songs)

        control = False



        while username != None:
            print("")
            print("")
            print("¿Qué deseas hacer?")
            print("""--> 1: Cambiar información del perfil
--> 2: Buscar (perfil, canción, playlist o album)
--> 3: Reproducir canción
--> 4: Otorgar un like
--> 5: Eliminar un like
--> 6: Crear una playlist
--> 7: Crear un album
--> 8: Subir una canción
--> 9: Eliminar la cuenta
--> 10: Estadísticas del programa
--> 11: Ver información - Base de datos
--> 0: Cerrar sesión""")

            x = input("Opción: ") 

            if x == "1":
                id_new_user = usuario_activo.id
                name_new_user = None
                username_new_user = None
                email_new_user = None
                type_new_user = usuario_activo.type
                username_guide = username
                streams_guide = int(usuario_activo.streams)
                while name_new_user == None:
                    x = input("Nombre: ")
                    y = True
                    for i in x:
                        if i.isnumeric() == True:
                            y = False
                            print("El nombre no debe tener números")
                            break

                    if y == True:
                        name_new_user = x

                while username_new_user == None: 
                    x = input("Username: ")
                    y = True
                    if x in all_usernames:
                        y = False
                        print("Ese usuario ya fue escogido")
                    if x not in all_usernames:
                        username_new_user = x
                
                while email_new_user == None: 
                    x = input("Email: ")
                    y = True
                    if "@" not in x:
                        y = False
                        print("Escriba un correo válido")
                    if "@" in x:
                        email_new_user = x

                if type_new_user == "listener":
                    users.remove(usuario_activo)
                    all_usernames.remove(usuario_activo.username)
                    usuario_activo = Listener(id_new_user, name_new_user, email_new_user, username_new_user, streams=streams_guide)
                    username = usuario_activo.username
                    users.append(usuario_activo)
                    all_usernames.append(username)
                    change_users_info(usuario_activo, username_guide)

                if type_new_user == "musician":
                    users.remove(usuario_activo)
                    all_usernames.remove(usuario_activo.username)
                    usuario_activo = Musician(id_new_user, name_new_user, email_new_user, username_new_user)
                    username = usuario_activo.username
                    users.append(usuario_activo)
                    all_usernames.append(username)
                    change_users_info(usuario_activo, username_guide)

            if x == "0":
                usuario_activo = None
                username = None

            if x == "6":
                if isinstance(usuario_activo, Musician) == True:
                    print("Los artistas no pueden crear playlists")
                if isinstance(usuario_activo, Listener) == True:
                    control = False
                    control_0 = False

                    while control != True:
                        id_new_playlist = str(uuid.uuid4())
                        name_new_playlist = None
                        description_new_playlist = None
                        creator_new_playlist = usuario_activo
                        tracklist_new_playlist = []

                        while name_new_playlist == None:
                            y = input("Nombre de la playlist: ")
                            if y in playlists_names:
                                print("Este nombre ya fue escogido")
                            if y not in playlists_names:
                                name_new_playlist = y

                        while description_new_playlist == None:
                            description_new_playlist = input("Descripción: ")

                        while control_0 != True:
                            print("""Si escribes el nombre de un artista, album o playlist
te saldrán todas las canciones que tiene cada uno""")
                            y = input("Canción a agregar: ")
                            if y in songs_names:
                                for i in songs:
                                    if y == i.name:
                                        cancion_playlist = i
                                        break
                                if cancion_playlist in tracklist_new_playlist:
                                    print("Ya agregaste esta canción")
                                if cancion_playlist not in tracklist_new_playlist:
                                    tracklist_new_playlist.append(cancion_playlist)

                            if y in albums_names:
                                for i in albums:
                                    if y == i.name:
                                        album_buscado = i
                                        break
                                buscador(album_buscado, users, songs, albums)

                            if y in all_usernames:
                                for i in users:
                                    if y == i.username:
                                        user_buscado = i
                                        break
                                buscador(user_buscado, users, songs, albums)

                            if y in playlists_names:
                                for i in playlists:
                                    if y == i.name:
                                        playlist_buscado = i
                                        break
                                buscador(playlist_buscado, users, songs, albums)

                            if len(tracklist_new_playlist) > 0: 
                                print("""--> 0: Ya agregué todas las canciones
--> 1: Seguir agregando canciones""")
                                k = input("Opción: ")
                                if k == "0":
                                    control_0 = True
                                else:
                                    pass

                        new_playlist = Playlist(id_new_playlist, name_new_playlist, description_new_playlist, creator_new_playlist, tracklist_new_playlist)
                        playlists.append(new_playlist)
                        playlists_names.append(new_playlist.name)
                        write_playlists(new_playlist)
                        control = True

            if x == "7": 
                if isinstance (usuario_activo, Listener) == True:
                    print("Los escuchas no pueden crear albums")
                if isinstance(usuario_activo, Musician) == True:
                    control = False
                    control_0 = False
                    my_songs, void = get_my_songs(usuario_activo, songs, 0)
                    if len(my_songs) == 0:
                        print("Primero tienes que subir tus canciones para crear un album")

                    if len(my_songs) > 0: 
                        while control != True:
                            id_new_album = str(uuid.uuid4())
                            name_new_album = None
                            description_new_album = None
                            cover_new_album = None
                            published_new_album = str(datetime.datetime.now())
                            genre_new_album = None
                            artist_new_album = usuario_activo
                            tracklist_new_album = []

                            while name_new_album == None:
                                y = input("Nombre del album: ")
                                if y in albums_names:
                                    print("Este nombre ya fue escogido")
                                if y not in albums_names:
                                    name_new_album = y

                            while description_new_album == None:
                                description_new_album = input("Descripción: ")

                            while cover_new_album == None:
                                y = input("Link de la portada del album: ")
                                if ":" in y and "." in y and "/" in y:
                                    cover_new_album = y
                                else:
                                    print("Escriba un link válido")

                            while genre_new_album == None:
                                genre_new_album = input("Género del album: ")

                            while control_0 != True:
                                mis_canciones, nombres_canciones = get_my_songs(usuario_activo, songs, 1)
                                y = input("Escoge las canciones que van en tu album: ")
                                if y in nombres_canciones:
                                    for i in mis_canciones:
                                        if y == i.name:
                                            cancion_album = i
                                            break
                                    if cancion_album in tracklist_new_album:
                                        print("Ya agregaste esta canción")
                                    if cancion_album not in tracklist_new_album:
                                        tracklist_new_album.append(cancion_album)
                                if y not in nombres_canciones:
                                    print("Escoge una de tus canciones")

                                if len(tracklist_new_album) > 0:
                                    print("""--> 0: Ya agregué todas las canciones
--> 1: Seguir agregando canciones""")
                                    k = input("Opción: ")
                                    if k == "0":
                                        control_0 = True
                                    else:
                                        pass

                            new_album = Album(id_new_album, name_new_album, description_new_album, cover_new_album, published_new_album, genre_new_album, artist_new_album, tracklist_new_album)
                            albums.append(new_album)
                            albums_names.append(new_album.name)
                            write_albums(new_album)     
                            control = True 

            if x == "8":
                if isinstance (usuario_activo, Listener) == True:
                    print("Los escuchas no pueden subir canciones")
                if isinstance(usuario_activo, Musician) == True:
                    control = False


                    while control != True:
                        id_new_song = str(uuid.uuid4())
                        name_new_song = None
                        duration_new_song = None
                        segundos_new_song = None
                        minutos_new_song = None
                        link_new_song = None
                        artist_new_song = usuario_activo

                        while name_new_song == None:
                            y = input("Nombre de la canción: ")
                            if y in songs_names:
                                print("Este nombre ya fue escogido")
                            if y not in songs_names:
                                name_new_song = y

                        while duration_new_song == None:
                            while minutos_new_song == None:
                                k = input("Minutos de duración (entre 0 y 10): ")
                                if k.isnumeric() == False:
                                    print("Escriba un número")
                                else:
                                    k = int(k)
                                    if k > 0 and k < 10:
                                        minutos_new_song = k
                            while segundos_new_song == None:
                                k = input("Segundos de duración (entre 0 y 60): ")
                                if k.isnumeric() == False:
                                    print("Escriba un número")
                                else:
                                    k = int(k)
                                    if k > 0 and k < 60:
                                        segundos_new_song = k

                            duration_new_song = str(minutos_new_song) + ":" + str(segundos_new_song)

                        while link_new_song == None:
                            y = input("Link de la canción: ")
                            if ":" in y and "." in y and "/" in y:
                                link_new_song = y
                            else:
                                print("Escriba un link válido")

                        new_song = Song(id_new_song, name_new_song, duration_new_song, link_new_song, artist_new_song)
                        songs.append(new_song)
                        songs_id.append(id_new_song)
                        songs_names.append(name_new_song)
                        write_songs(new_song)
                        control = True

            if x == "5":
                if isinstance (usuario_activo, Musician) == True:
                    print("Los artistas no pueden dar like")
                if isinstance(usuario_activo, Listener) == True:
                    control = False
                    objeto_likeado = None
                    while control != True:
                        likes_dados = get_likes_watch(username, users_id, playlists_id, albums_id, songs_id, users, playlists, albums, songs)
                        if len(likes_dados) == 0:
                            print("No le ha dado like a nada")
                            control = True
                        if len(likes_dados) > 0:
                            print("""Escriba el nombre de lo que desea eliminar su like
--> 0: Salir""")
                            y = input("Nombre: ")
                            if y == "0":
                                control = True
                            if y not in likes_dados:
                                print("Escriba un nombre válido")
                            if y in likes_dados:
                                if y in all_usernames:
                                    for i in users:
                                        if y == i.username:
                                            objeto_sin_like = i.id
                                            break
                                if y in albums_names:
                                    for i in albums:
                                        if y == i.name: 
                                            objeto_sin_like = i.id
                                            break 
                                if y in playlists_names:
                                    for i in playlists:
                                        if y == i.name: 
                                            objeto_sin_like = i.id
                                            break 
                                if y in songs_names:
                                    for i in songs:
                                        if y == i.name: 
                                            objeto_sin_like = i.id
                                            break 

                                delete_likes(username, objeto_sin_like)
                                control = True

            if x == "4":
                if isinstance (usuario_activo, Musician) == True:
                    print("Los artistas no pueden dar like")
                if isinstance(usuario_activo, Listener) == True:
                    control = False
                    objeto_likeado = None
                    while control != True:
                        print("""Escribe el nombre de una de estas para darle like:
--> Artista (nombre de usuario)
--> Canción
--> Playlist
--> Album
--> 0: Salir""")
                        
                        y = input("Nombre: ")

                        if y == "0":
                            control = True

                        if y in all_usernames:
                            for i in users:
                                if i.username == y:
                                    if isinstance(i, Listener) == True:
                                        print("No se le puede otorgar un like a un escucha")
                                        break

                                    if isinstance(i, Musician) == True:
                                        objeto_likeado = i
                                        write_likes(username, objeto_likeado)
                                        users = get_listener_likes(users)
                                        users = get_likes(users)
                                        control = True
                                        break

                        if y in songs_names:
                            for i in songs:
                                if i.name == y:
                                    objeto_likeado = i
                                    write_likes(username, objeto_likeado)
                                    users = get_listener_likes(users)
                                    songs = get_likes(songs)
                                    control = True
                                    break

                        if y in albums_names:
                            for i in albums:
                                if i.name == y:
                                    objeto_likeado = i
                                    write_likes(username, objeto_likeado)
                                    users = get_listener_likes(users)
                                    albums = get_likes(albums)
                                    control = True
                                    break

                        if y in playlists_names:
                            for i in playlists:
                                if i.name == y:
                                    objeto_likeado = i
                                    write_likes(username, objeto_likeado)
                                    users = get_listener_likes(users)
                                    playlists = get_likes(playlists)
                                    control = True
                                    break

                        if y not in all_usernames:
                            if y not in songs_names:
                                if y not in playlists_names:
                                    if y not in albums_names:
                                        print("Escriba un nombre válido")


            if x == "3":
                control = False
                cancion = None
                while control != True:
                    print("""Escriba el nombre de la canción a reproducir:
--> Si escribe el nombre de un artista, playlist o album
se le mostrarán las distintas canciones que posee cada uno
--> Se abrirá el link de la canción en el navegador de su computadora
--> 0: Salir""")
                    
                    y = input("Nombre de la canción: ")
                    if y == "0":
                        control = True

                    if y in songs_names:
                        for i in songs:
                            if y == i.name:
                                cancion = i
                                control = True
                                streams_listener(usuario_activo)
                                reproducciones_cancion(i)
                                cancion.play()
                                break

                    if y in all_usernames:
                        for i in users:
                            if y == i.username:
                                if isinstance(i, Listener) == True:
                                    print("Escriba el nombre de un artista, no el de un escucha")
                                    break
                                if isinstance(i, Musician) == True:
                                    get_artist_info(users, y, albums, songs)
                                    break

                    if y in albums_names:
                        for i in albums:
                            if y == i.name:
                                buscador(i, users, songs, albums)
                                break

                    if y in playlists_names:
                        for i in playlists:
                            if y == i.name:
                                buscador(i, users, songs, albums)
                                break

                    if y not in all_usernames:
                        if y not in songs_names:
                            if y not in playlists_names:
                                if y not in albums_names:
                                    print("Escriba un nombre válido")

            if x == "2":
                control = False
                while control != True:
                    print("""Escriba el nombre de:
--> Artista (nombre de usuario)
--> Canción
--> Playlist
--> Album
--> 0: Salir""")
                    y = input("Inserte el nombre de lo que desea buscar: ")

                    if y == "0":
                        control = True

                    if y in all_usernames:
                        for i in users:
                            if y == i.username:
                                if isinstance(i, Musician) == True:
                                    objeto_buscado = i
                                    username_buscado = i.username
                                    get_artist_info(users, username_buscado, albums, songs)
                                    control = True
                                    break

                                if isinstance(i, Listener) == True:
                                    objeto_buscado = i
                                    username_buscado = i.username
                                    print(get_listener_info(users, username_buscado, albums, songs, playlists, albums_id, songs_id, playlists_id))
                                    control = True
                                    break

                    if y in songs_names: 
                        for i in songs:
                            if y == i.name:
                                objeto_buscado = i
                                buscador(objeto_buscado, users, songs, albums)
                                control = True
                                break
                    
                    if y in albums_names: 
                        for i in albums:
                            if y == i.name:
                                objeto_buscado = i
                                buscador(objeto_buscado, users, songs, albums)
                                control = True
                                break

                    if y in playlists_names: 
                        for i in playlists:
                            if y == i.name:
                                objeto_buscado = i
                                buscador(objeto_buscado, users, songs, albums)
                                control = True
                                break
                    
                    if y not in all_usernames:
                        if y not in songs_names:
                            if y not in playlists_names:
                                if y not in albums_names:
                                    print("Escriba un nombre válido")

            if x == "9":
                control = False
                while control != True:
                    y = input("Seguro? (si) o (no): ")
                    if y == "si":
                        if usuario_activo in users:
                            users.remove(usuario_activo)
                        if username in all_usernames:
                            all_usernames.remove(username)
                        delete_user(usuario_activo)
                        usuario_activo = None
                        username = None
                        control = True
                    if y == "no":
                        control = True
                    else:
                        print("Escoja 'si' o 'no'")

            if x == "10":
                control = False
                control_0 = False
                x_artists, y_artists, x_listeners, y_listeners, x_albums, y_albums, x_songs, y_songs = top_5(users, albums, songs, 0)
                while control != True:
                    print("""--> 1: Ver top 5 con más streams
--> 2: Ver gráficas
--> 0: Salir""")
                    y = input("Opción: ")
                    if y == "0":
                        control = True

                    if y == "1":
                        top_5(users, albums, songs, 1)

                    if y == "2":
                        control_0 = False
                        while control_0 != True:
                            print("""--> 1: Ver gráfica de los artistas
--> 2: Ver gráfica de los escuchas
--> 3: Ver gráfica de los albums
--> 4: Ver gráfica de las canciones""")
                            y = input("Opción: ")
                            if y == "1":
                                pyplot.scatter(x_artists, y_artists)
                                pyplot.show()
                                control_0 = True

                            if y == "2": 
                                pyplot.scatter(x_listeners, y_listeners)
                                pyplot.show()
                                control_0 = True

                            if y == "3":
                                pyplot.scatter(x_albums, y_albums)
                                pyplot.show()
                                control_0 = True

                            if y == "4":
                                pyplot.scatter(x_songs, y_songs)
                                pyplot.show()
                                control_0 = True

            if x == "11":
                control = False
                while control != True:
                    print("""Ver usuarios y nombres de: 
--> 1: Usuarios
--> 2: Canciones
--> 3: Albums
--> 4: Playlists
--> 0: Salir""")
                    y = input("Opción: ")
                    
                    if y == "0":
                        control = True
                    if y == "1":
                        print(all_usernames)
                    if y == "2":
                        print(songs_names)
                    if y == "3":
                        print(albums_names)
                    if y == "4":
                        print(playlists_names)



main()