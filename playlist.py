# Fabio Carrozza. C.I: 30714977. Proyecto: Metrotify

class Playlist:
    """Esta clase contiene las playlists creadas
    por los usuarios de tipo Listener"""

    def __init__(self, id, name, description, creator, tracklist, likes=0, streams=0):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracklist = tracklist
        self.likes = likes
        self.streams = streams

    def show(self):
        return f"""Nombre: {self.name} -- Descripción: {self.description}
Likes: {self.likes} -- Reproducciones: {self.streams}"""