# Fabio Carrozza. C.I: 30714977. Proyecto: Metrotify

import webbrowser

class Song: 
    """Esta es la clase que contiene las canciones, 
    tanto en las playlists como en los albums"""

    def __init__(self, id, name, duration, link, artist, likes=0, streams=0): 
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.artist = artist
        self.likes = likes
        self.streams = streams

    def show(self):
        return f"""Nombre: {self.name} -- Duración: {self.duration}
Likes: {self.likes} -- Reproducciones: {self.streams} """
    
    def play(self):
        webbrowser.open(self.link)