# Fabio Carrozza. C.I: 30714977. Proyecto: Metrotify

class Album: 
    """Esta es la clase que contiene los albums
    creados por los usuarios de tipo Musician"""

    def __init__(self, id, name, description, cover, published, genre, artist, tracklist, likes=0, streams=0):
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist
        self.likes = likes
        self.streams = streams

    def show(self):
        return f"""Nombre: {self.name} -- Descripción: {self.description}
Género: {self.genre} -- Reproducciones: {self.streams} -- Likes: {self.likes}"""