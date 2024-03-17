# Fabio Carrozza. C.I: 30714977. Proyecto: Metrotify

import matplotlib
import os
import requests
import json
import random
from playlist import Playlist
from album import Album
from song import Song
from user import Listener, Musician

def json_files():
    """Esta función crea los archivos JSON, si es que no existen,
    a partir de los links del Git"""

    # Se escriben los paths de cada json
    path_users = "./users.json"
    path_albums = "./albums.json"
    path_playlists = "./playlists.json"
    check_users = os.path.isfile(path_users)
    check_albums = os.path.isfile(path_albums)
    check_playlists = os.path.isfile(path_playlists)

    # Se leen los links
    if check_users == False:
        users_0 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
        users = users_0.json()
    if check_albums == False:
        albums_0 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
        albums = albums_0.json()
    if check_playlists == False:
        playlists_0 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
        playlists = playlists_0.json()

    # Se escriben los archivos JSON
    if check_users == False:
        archivo = open("users.json", "w", encoding="utf-8")
        json.dump(users, archivo)
        archivo.close() 

    if check_albums == False:
        archivo = open("albums.json", "w", encoding="utf-8")
        json.dump(albums, archivo)
        archivo.close()

    if check_playlists == False:
        archivo = open("playlists.json", "w", encoding="utf-8")
        json.dump(playlists, archivo)
        archivo.close()

def download_users():
    """Retorna una lista con todos los usuarios ya establecidos como objetos.
    Esta función lee el API y la base de datos en el txt para crear
    los usuarios del programa"""

    # Esta es la lista donde se adjuntarán los objetos creados
    users = []

    # Se lee el API
    archivo = open("users.json", "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    # Se realiza un ciclo para crear los objetos desde la API
    for i in datos:
        if i["type"] == "listener":
            y = random.randrange(100, 1000)
            users.append(Listener(i["id"], i["name"], i["email"], i["username"], streams=y))
        
        if i["type"] == "musician":
            users.append(Musician(i["id"], i["name"], i["email"], i["username"]))

    # Se realiza un ciclo para crear los objetos desde la base de datos txt
    if len(db["new_users"]) >= 1:
        z = db["new_users"]
        for i in z:
            if i["type"] == "listener":
                users.append(Listener(i["id"], i["name"], i["email"], i["username"], streams=i["streams"], likes=i["likes"]))
        
            if i["type"] == "musician":
                users.append(Musician(i["id"], i["name"], i["email"], i["username"], streams=i["streams"], likes=i["likes"]))
    
    return users


def download_songs(users):
    """Retorna las canciones como objetos en una lista.
    Esta función analiza el API y la base de datos en el txt 
    para crear los objetos de las canciones"""

    # Esta es la lista donde se adjuntarán los objetos creados
    songs = []

    # Se lee el API
    archivo = open("albums.json", "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    # Se realiza un ciclo para crear los objetos desde la API
    for i in datos:
        for j in i["tracklist"]:
            for z in users:
                if i["artist"] == z.id:
                    artist = z
            y = random.randrange(1000, 100000)
            songs.append(Song(j["id"], j["name"], j["duration"], j["link"], artist, streams=y))

    # Se realiza un ciclo para crear las canciones desde el txt
    if len(db["songs_new"]) >= 1:
        f = db["songs_new"]
        for i in f: 
            for j in users: 
                if i["artist"] == j.id:
                    artist = j
            songs.append(Song(i["id"], i["name"], i["duration"], i["link"], artist, streams=i["streams"]))

    return songs

def download_albums(users, songs):
    """Retorna los albums como objetos en una lista.
    Esta función analiza el API y la base de datos en el txt 
    para crear los objetos de los albums"""

    # Esta es la lista donde se adjuntarán los objetos creados
    albums = []

    # Se lee el API
    archivo = open("albums.json", "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    # Se realiza un ciclo para crear los objetos desde la API
    for i in datos:
        canciones = []
        reproducciones = []
        for j in users: 
            if i["artist"] == j.id:
                artist = j
        
        for z in i["tracklist"]: 
            for w in songs:
                if z["id"] == w.id:
                    canciones.append(w)
                    reproducciones.append(w.streams)

        albums.append(Album(i["id"], i["name"], i["description"], i["cover"], i["published"], i["genre"], artist, canciones, streams=sum(reproducciones)))

    # Se realiza un ciclo para crear los objetos desde el txt
    if len(db["albums_new"]) >= 1:
        f = db["albums_new"]
        for i in f:
            canciones = []
            reproducciones = []
            for j in users: 
                if i["artist"] == j.id:
                    artist = j

            for z in i["tracklist"]: 
                for w in songs:
                    if z == w.id:
                        canciones.append(w)
                        reproducciones.append(w.streams)

            albums.append(Album(i["id"], i["name"], i["description"], i["cover"], i["published"], i["genre"], artist, canciones, streams=sum(reproducciones)))

    return albums

def download_playlists(users, songs):
    """Retorna los playlists como objetos en una lista.
    Esta función analiza el API y la base de datos en el txt 
    para crear los objetos de los playlists"""

    # Esta es la carpeta donde se adjuntarán los objetos
    playlists = []

    # Se lee el API
    archivo = open("playlists.json", "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    # Se realiza un ciclo para crear los objetos desde la API
    for i in datos:
        canciones = []
        reproducciones = []
        for j in users: 
            if i["creator"] == j.id:
                listener = j
        
        for z in i["tracks"]: 
            for w in songs:
                if z == w.id:
                    canciones.append(w)
                    reproducciones.append(w.streams)

        playlists.append(Playlist(i["id"], i["name"], i["description"], listener, canciones, streams=sum(reproducciones)))

    # Se realiza un ciclo para crear los objetos desde el archivo txt
    if len(db["playlists_new"]) >= 1:
        f = db["playlists_new"]
        for i in f:
            canciones = []
            reproducciones = []
            for j in users: 
                if i["creator"] == j.id:
                    listener = j
            
            for z in i["tracks"]: 
                for w in songs:
                    if z == w.id:
                        canciones.append(w)
                        reproducciones.append(w.streams)

            playlists.append(Playlist(i["id"], i["name"], i["description"], listener, canciones, streams=sum(reproducciones)))

    return playlists

def get_artist_streams(users, songs):
    """Esta función retorna las reproducciones que tiene cada artista
    tomando en cuenta las canciones y sus streams"""

    # Se realiza un ciclo para asignarle a cada artista sus respectivas reproducciones
    for i in songs:
        for j in users:
            if isinstance(j, Musician) == True:
                if i.artist == j:
                    j.streams += i.streams
                    break
    
    return users

def get_likes(x):
    """Esta función asigna y retorna los likes de cada objeto
    a partir del archivo txt donde se almacena el historial"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db["likes_users"]

    # Se realiza un ciclo para analizar los id del diccionario y asignar los likes
    for i in z:
        for j in i["likes"]:
            for a in x:
                if j == a.id:
                    a.likes += 1

    return x

def get_listener_likes(x):
    """Esta función retorna los likes que puso cada escucha en su sesión
    basándose en la base de datos del txt"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db["likes_users"]

    # Se realiza un ciclo para asignar los likes
    for i in z:
        y = len(i["likes"])
        for a in x:
            if isinstance(a, Listener) == True:
                if a.username == i["username"]:
                    a.likes = y

    return x

def get_id(x):
    """Esta función retorna una lista con todos los id
    que tienen los objetos de una clase"""

    # En esta lista se guardarán todos los id de esa clase
    id = []

    for i in x:
        id.append(i.id)

    return id

def get_listener_info(users, username, albums, songs, playlists, albums_id, songs_id, playlists_id):
    """Esta función retorna la información sobre los likes
    y las playlists creadas por un usuario"""

    playlists_creados = []
    playlists_guardados = []
    albumes_gustados = []
    canciones_gustadas = []

    for i in users:
        if username == i.username:
            usuario = i
            break

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db["likes_users"]

    for i in z:
        if i["username"] == usuario.username:
            for j in i["likes"]:
                if j in songs_id:
                    for w in songs:
                        if w.id == j:
                            canciones_gustadas.append(w.name)
                            break

                if j in albums_id:
                    for w in albums:
                        if w.id == j:
                            albumes_gustados.append(w.name)
                            break

                if j in playlists_id:
                    for w in playlists:
                        if w.id == j:
                            playlists_guardados.append(w.name)

    for i in playlists:
        if i.creator == usuario:
            playlists_creados.append(i.name)

    return f"""{usuario.username} este es tu historial
--> Playlists guardados: {playlists_guardados}
--> Playlists creados: {playlists_creados}
--> Albums gustados: {albumes_gustados}
--> Canciones gustadas: {canciones_gustadas}""" 

def get_artist_info(users, username, albums, songs):
    """Esta función retorna el historial del usuario
    en caso de que sea de tipo Musician"""

    albums_propios = []
    songs_propios = []
    canciones_0 = []
    streams = []
    final_streams = []

    for i in users:
        if username == i.username:
            usuario = i
            break

    for i in albums: 
        if i.artist == usuario:
            albums_propios.append(i)

    for i in songs:
        if i.artist == usuario:
            songs_propios.append(i)

    for i in songs_propios:
        canciones_0.append({"name": i.name, "streams": i.streams})

    for i in canciones_0:
        streams.append(i["streams"])

    for _ in streams:
        if len(final_streams) < 10:
            y = max(streams)
            for j in canciones_0:
                if j["streams"] == y:
                    final_streams.append(j)
                    streams.remove(y)
                    break

    print(f"{usuario.username} este es tu historial")

    for i in albums_propios:
        print("Album")
        print(i.name)
        tracklist = []
        for j in i.tracklist:
            tracklist.append(j.name)
        print(f"Tracklist: {tracklist}")

    print("Canciones más escuchadas")
    for i in range(len(final_streams)):
        print(f"Canción {i + 1}")
        print(f"{final_streams[i]['name']} -- {final_streams[i]['streams']} reproducciones")

    print(f"Reproducciones totales: {usuario.streams}")

def get_usernames(x):
    """Esta función retorna una lista con todos los usernames"""

    usernames = []

    # Se realiza un ciclo para obtener todos los usernames
    for i in x: 
        usernames.append(i.username)

    return usernames

def get_names(x):
    """Esta función retorna una lista con todos los nombres de esa clase"""

    names = []

    # Se realiza un ciclo para obtener todos los nombres
    for i in x:
        names.append(i.name)

    return names

def write_users(x):
    """Esta función escribe los nuevos usuarios en el txt"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    y = {"id": x.id, "name": x.name, "email": x.email, "username": x.username, "type": x.type, "streams": x.streams, "likes": x.likes}

    z["new_users"].append(y)

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def change_users_info(x, y):
    """Esta función modifica la información del usuario en el txt"""
    
    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    for i in z["new_users"]:
        if x.id == i["id"]:
            z["new_users"].remove(i)
            break

    for i in z["likes_users"]:
        if i["username"] == y:
            i["username"] = x.username
            break

    y = {"id": x.id, "name": x.name, "email": x.email, "username": x.username, "type": x.type, "streams": x.streams, "likes": x.likes}

    z["new_users"].append(y)

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def buscador(x, users, songs, albums):
    """Esta es una función que imprime la información del
    objeto en cuestión que se busca"""

    if isinstance(x, Musician) == True:
        canciones = []
        albumes = []
        print(x.showWork())
        for i in songs:
            if i.artist == x:
                canciones.append(i.name)

        for i in albums:
            if i.artist == x:
                albumes.append(i.name)

        print(f"Canciones: {canciones}")
        print(f"Albums: {albumes}")

    if isinstance(x, Song) == True:
        print(x.show())
        for i in users:
            if i == x.artist:
                artista = i.name
                username = i.username

        print(f"Compositor: {artista} -- User: {username}")

    if isinstance(x, Playlist) == True:
        canciones = []
        print(x.show())
        for i in songs:
            for j in x.tracklist:
                if i == j:
                    canciones.append(i.name)

        for i in users:
            if i == x.creator:
                artista = i.name
                username = i.username
                break

        print(f"Canciones del playlist: {canciones}")
        print(f"Creador: {artista} -- User: {username}")

    if isinstance(x, Album) == True:
        canciones = []
        for i in songs:
            for j in x.tracklist:
                if i == j:
                    canciones.append(i.name)

        for i in users:
            if i == x.artist:
                artista = i.name
                username = i.username
                break

        print(f"Canciones del album: {canciones}")
        print(f"Compositor: {artista} -- User: {username}")

def delete_user(x):
    """Esta función elimina la información del usuario en el txt"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    for i in z["new_users"]:
        if x.id == i["id"]:
            z["new_users"].remove(i)
            break

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def streams_listener(x):
    """Esta función escribe los streams dados por el usuario activo"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    for i in z["new_users"]:
        if i["username"] == x.username:
            i["streams"] += 1
            break

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def reproducciones_cancion(x):
    """Esta función suma los streams que recibió la canción"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    for i in z["songs_new"]:
        if i["name"] == x.name:
            i["streams"] += 1
            break

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def write_likes(username, object):
    """Esta función escribe el id del objeto 
    likeado en el usuario correspondiente en el txt"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db
    usuarios = []

    for i in z ["likes_users"]:
        usuarios.append(i["username"])

    if username in usuarios:
        for i in z["likes_users"]:
            if username == i["username"]:
                if object.id in i["likes"]:
                    break
                if object.id not in i["likes"]:
                    i["likes"].append(object.id)
                    break
    if username not in usuarios:
        y = {"username": username, "likes": [object.id]}
        z["likes_users"].append(y)

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def get_likes_watch(username, users_id, playlists_id, albums_id, songs_id, users, playlists, albums, songs):
    """Esta función lee los likes de cada usuario"""

    likes_playlists = []
    likes_songs = []
    like_albums = []
    like_artists = []

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    for i in z["likes_users"]:
        if username == i["username"]:
            for j in i["likes"]:
                if j in users_id:
                    for a in users:
                        if j == a.id:
                            like_artists.append(a.username)
                            break
                if j in playlists_id:
                    for a in playlists:
                        if j == a.id:
                            likes_playlists.append(a.name)
                            break
                if j in albums_id:
                    for a in albums:
                        if j == a.id:
                            like_albums.append(a.name)
                            break
                if j in songs_id:
                    for a in songs:
                        if j == a.id:
                            likes_songs.append(a.name)
                            break

    print(f"""Artistas gustados: {like_artists}
Canciones gustadas: {likes_songs}
Albums gustados: {like_albums}
Playlists gustados: {likes_playlists}""")
    
    return likes_songs + like_artists + likes_playlists + like_albums

def delete_likes(username, id):
    """Esta función elimina el id de la lista de likes del usuario"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    for i in z["likes_users"]:
        if username == i["username"]:
            for j in i["likes"]:
                if id == j:
                    i["likes"].remove(j)
                    break

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def write_songs(song):
    """Esta función escribe la nueva canción agregada al programa"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    y = {"id": song.id, "name": song.name, "duration": song.duration, "link": song.link, "artist": (song.artist).id, "streams": song.streams}

    z["songs_new"].append(y)

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def get_my_songs(user, songs, x):
    """Esta función retorna las canciones compuestas
    por un artista en específico"""

    mis_canciones = []
    nombres_canciones = []

    for i in songs:
        if i.artist == user:
            mis_canciones.append(i)

    for i in mis_canciones:
        nombres_canciones.append(i.name)

    if x == 1:
        print(f"Tus canciones: {nombres_canciones}")

    return mis_canciones, nombres_canciones

def write_albums(album):
    """Esta función escribe el nuevo album agregado al programa"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    tracklist = []

    for i in album.tracklist:
        tracklist.append(i.id)

    y = {"id": album.id, "name": album.name, "description": album.description, "cover": album.cover, "published": album.published, "genre": album.genre, "artist": (album.artist).id,
         "tracklist": tracklist}
    
    z["albums_new"].append(y)

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def write_playlists(playlist):
    """Esta función escribe la nueva playlist agregada al programa"""

    # Se lee el txt
    archivo = open("datos.txt", "r", encoding="utf-8")
    db = json.load(archivo)
    archivo.close()

    z = db

    tracklist = []

    for i in playlist.tracklist:
        tracklist.append(i.id)

    y = {"id": playlist.id, "name": playlist.name, "description": playlist.description, 
         "creator": (playlist.creator).id, "tracks": tracklist}
    
    z["playlists_new"].append(y)

    # Se reescribe el txt
    archivo = open("datos.txt", "w", encoding="utf-8")
    json.dump(z, archivo)
    archivo.close()

def top_5(users, albums, songs, x):
    """Esta función imprime los top 5 artistas, albums
    y canciones con más streams de todo el programa"""

    users_only_streams = []
    albums_only_streams = []
    listeners_only_streams = []
    songs_only_streams = []

    for i in users:
        if isinstance(i, Musician) == True:
            users_only_streams.append(i.streams)
        if isinstance(i, Listener) == True:
            listeners_only_streams.append(i.streams)

    for i in albums:
        albums_only_streams.append(i.streams)

    for i in songs:
        songs_only_streams.append(i.streams)

    users_only_streams.sort(reverse=True)
    albums_only_streams.sort(reverse=True)
    songs_only_streams.sort(reverse=True)
    listeners_only_streams.sort(reverse=True)

    users_streams = []
    albums_streams = []
    songs_streams = []
    listener_streams = []

    top_5_artists = []
    top_5_listeners = []
    top_5_songs = []
    top_5_albums = []
    

    for i in users_only_streams:
        for j in users:
            if isinstance(j, Musician) == True:
                if i == j.streams:
                    users_streams.append({"username": j.username, "streams": i})

    for i in listeners_only_streams:
        for j in users:
            if isinstance(j, Listener) == True:
                if i == j.streams:
                    listener_streams.append({"username": j.username, "streams": i})

    for i in albums_only_streams:
        for j in albums:
            if i == j.streams:
                albums_streams.append({"name": j.name, "streams": i})

    for i in songs_only_streams:
        for j in songs:
            if i == j.streams:
                songs_streams.append({"name": j.name, "streams": i})

    for i in range(0, 5):
        top_5_artists.append(users_streams[i])
        top_5_listeners.append(listener_streams[i])
        top_5_albums.append(albums_streams[i])
        top_5_songs.append(songs_streams[i])

    if x == 1:
        print("")
        print("Artistas con más streams")
        for i in range(5):
            print(f"{i+1}: {top_5_artists[i]['username']} -- {top_5_artists[i]['streams']}")

        print("")
        print("Escuchas con más streams")
        for i in range(5):
            print(f"{i+1}: {top_5_listeners[i]['username']} -- {top_5_listeners[i]['streams']}")

        print("")
        print("Canciones con más streams")
        for i in range(5):
            print(f"{i+1}: {top_5_songs[i]['name']} -- {top_5_songs[i]['streams']}")

        print("")
        print("Albums con más streams")
        for i in range(5):
            print(f"{i+1}: {top_5_albums[i]['name']} -- {top_5_albums[i]['streams']}")

    x_users = []
    y_users = []
    x_listeners = []
    y_listeners = []
    x_albums = []
    y_albums = []
    x_songs = []
    y_songs = []

    for i in top_5_artists:
        x_users.append(i["username"])
        y_users.append(i["streams"])

    for i in top_5_listeners:
        x_listeners.append(i["username"])
        y_listeners.append(i["streams"])

    for i in top_5_albums:
        x_albums.append(i["name"])
        y_albums.append(i["streams"])

    for i in top_5_songs:
        x_songs.append(i["name"])
        y_songs.append(i["streams"])

    return x_users, y_users, x_listeners, y_listeners, x_albums, y_albums, x_songs, y_songs