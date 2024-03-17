# Fabio Carrozza. C.I: 30714977. Proyecto: Metrotify

class User:
    """ Esta es la clase principal del Proyecto. 
    De esta clase se heredan las clases Listener (Escucha) y Musician (Artista)"""

    def __init__(self, id, name, email, username, type):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.type = type

    def read(self):
        return
    

class Listener: 
    """Esta clase se hereda de la clase User.
    Esta sería la clase para los usuarios que no son artistas"""

    def __init__(self, id, name, email, username, type="listener", streams=0, likes=0):
        User.__init__(self, id, name, email, username, type)
        self.streams = streams
        self.likes = likes

    def showInfo(self):
        return f"""Nombre: {self.name} -- Correo: {self.email} -- Tipo de cuenta: Escucha
Username: {self.username} -- Reproducciones: {self.streams} -- Likes: {self.likes}"""
    

class Musician:
    """Esta clase se hereda de la clase User. 
    Esta sería la clase para los usuarios que desean subir sus canciones y albums"""

    def __init__(self, id, name, email, username, type="musician", streams=0, likes=0):
        User.__init__(self, id, name, email, username, type)
        self.streams = streams
        self.likes = likes

    def showWork(self):
        return f"""Nombre: {self.name} -- Correo: {self.email} -- Tipo de cuenta: Artista -- Username: {self.username}
Reproducciones totales de sus canciones: {self.streams} -- Likes a sus canciones: {self.likes}"""