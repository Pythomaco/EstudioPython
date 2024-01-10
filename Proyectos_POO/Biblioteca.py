#!usr/bin/env python3

class LIBRO:
    def __init__(self, idLibro, autor, titulo):
        self.idLibro = idLibro
        self.autor = autor
        self.titulo = titulo
        self.prestado = False

    def __str__(self):
        return f"""LIBRO Nº {self.idLibro}:
    TÍTULO: {self.titulo}
    AUTOR: {self.autor}"""

    def __repr__(self):
        return self.__str__()

class BIBLIOTECA:
    def __init__(self):
        self.libros = {} 
    def agregarLibro(self, libro):
        if libro.idLibro not in self.libros:
            self.libros[libro.idLibro] = libro
        else:
            print(f"""[!] No es posible agregar el libro con ID {libro.idLibro}.""")
    def prestarLibro(self, idLibro):
        if idLibro in self.libros and not self.libros[idLibro].prestado:
            self.libros[idLibro].prestado = True
        else:
            print(f"""[!] No es posible prestar el libro con ID {idLibro}""")

    @property
    def mostrarLibros(self):
        return [libro for libro in self.libros.values() if not libro.prestado]

    @property
    def mostrarLibrosPrestados(self):
        return [libro for libro in self.libros.values() if libro.prestado]

class BIBLIOTECA_INFANTIL(BIBLIOTECA):
    def __init__(self):
        super().__init__()
        self.librosInfantiles = {} # {1: False, 2: True}

    def agregarLibro(self, libro, esinfantil):
        super().agregarLibro(libro)
        self.librosInfantiles[libro.idLibro] = esinfantil

    def prestarLibro(self, idLibro, esNino):
        if idLibro in self.libros and not self.libros[idLibro].prestado and self.librosInfantiles[idLibro] == esNino:
           self.libros[idLibro].prestado = True
        else:
            print(f"""[!] No es posible prestar el libro con ID {idLibro}""")

    @property
    def mostrarEsinfantil(self):
        return self.librosInfantiles

if __name__ == '__main__':

    biblioteca = BIBLIOTECA_INFANTIL()

    libro1 = LIBRO(1, "Lawrence", "La odisea de un bajo")
    libro2 = LIBRO(2, "Menganito Rodríguez", "Pinta y colorea")

    biblioteca.agregarLibro(libro1, esinfantil = False)
    biblioteca.agregarLibro(libro2, esinfantil = True)

    print(f"""[+] Libros en la biblioteca: {biblioteca.mostrarLibros}
    """)

    biblioteca.prestarLibro(1, esNino = True)

    print(f"""[+] Libros en la biblioteca: {biblioteca.mostrarLibros}
    """)

    print(f"""[+] Libros prestados: {biblioteca.mostrarLibrosPrestados}
    """)

    print(f"""[+] Libros infantiles: {biblioteca.mostrarEsinfantil}
    """)
