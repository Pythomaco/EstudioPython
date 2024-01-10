#!usr/bin/env python3

class Animal:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False
    
    def alimentar(self):
        self.alimentado = True

    def __str__(self):
        return f"""{self.nombre} ({self.especie}) - {'Alimentado' if self.alimentado else 'Hambriento'}"""

    def vender(self):
        self.alimentado = False     
    
class TiendaAnimales:

    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)
    
    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()
    
    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                self.animales.remove(animal)
                return
        print (f""" [!] No se ha encontrado ningún animal en al tienda con nombre {nombre}.
    """)
            

if __name__ == '__main__':

    tienda = TiendaAnimales("Dimi")

    gato = Animal ("Lastra", "Gato")
    perro = Animal ("Pachón", "Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)

    tienda.mostrar_animales()
    tienda.alimentar_animales()

    print(f"""[+] Mostrando si los animales han sido alimentados:
    """)

    tienda.mostrar_animales()

    tienda.vender_animal("Lastra")

    print(f""" [+] Mostrando los animales una vez Lastra ha sido vendida:
    """)

    tienda.mostrar_animales()