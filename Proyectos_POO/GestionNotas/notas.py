#!usr/bin/env python3

class Nota:

    def __init__(self, contenido):
        self.contenido = contenido

    def __str__(self):
        return self.contenido
    
    def coincide(self, busqueda):
        return busqueda in self.contenido