#!usr/bin/env python3

import pickle

##################################################################
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre} - {self.edad} años"

###################################################
def agregar_persona():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nueva_persona = Persona (nombre, edad)
    return nueva_persona

def guardar_lista(lista):
    with open('gente.pkl', 'wb') as archivo:
        pickle.dump(lista, archivo)

def cargar_lista():
    try:
        with open('gente.pkl', 'rb') as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return []
    
def eliminar_persona(lista):
    if not lista:
        print ("La lista está vacía.")
        return
    print("Lista de personas:")
    for i, persona in enumerate(lista):
        print(f"{i}) {persona}")
    try:
        indice = int(input("Ingresa el número de la persona: "))
        if 0 <= indice < len(lista):
            persona_eliminada = lista.pop(indice)
            print(f"Persona eliminada: {persona_eliminada}")
        else:
            print("[!] Índice no válido.")
    except ValueError:
        print("[!] Ingresa un número válido.")
######################################################################################
def main():
    gente = cargar_lista()

    while True:

        accion = input("""¿Qué quieres hacer?
                    1) Mostrar lista
                    2) Añadir
                    3) Guardar lista actual
                    4) Cargar lista guardada
                    5) Eliminar
                    x) Salir
                       """)
        if accion == "2":
            nueva_persona = agregar_persona()
            gente.append(nueva_persona)
            print(f"""Se ha añadido un nuevo miembro a la lista: {nueva_persona.nombre} - {nueva_persona.edad} años""")
        elif accion == "x":
            print(f"""Saliendo del programa...""")
            break
        elif accion == "1":
            print("Lista de personas:")
            for persona in gente:
                print (persona)
        elif accion == "3":
                guardar_lista(gente)
                print("Lista guardada con éxito.")
        elif accion == "4":
            gente = cargar_lista()
        elif accion == "5":
            eliminar_persona(gente)            
        else:
            print("Opción no válida.")

#########################################################################################
if __name__ == "__main__":
    main()
