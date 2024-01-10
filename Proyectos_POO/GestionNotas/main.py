#!usr/bin/env python3

import os
from gestor_notas import GestorNotas

def main():

    gestor = GestorNotas()

    while True:
        print(f"---------------MENÚ---------------")
        print(f"1. Agregar una nota")
        print(f"2. Leer todas las notas")
        print(f"3. Buscar por una nota")
        print(f"4. Eliminar una nota")
        print(f"5. Salir")

        opcion = input(f"\n[\u270E] Escoge una opción: ")

        if opcion == "1":
            contenido = input(f"\n[\u270E] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "2":
            notas = gestor.leer_notas()
            print("[+] Mostrando todas las notas almacenadas:\n")
            for i, nota in enumerate(notas):
                print(f"´{i}: {nota}")

        elif opcion == "3":
            busqueda = input("\n[\u270E] Ingresa tu búsqueda: ")

            print(f"\n[i] Notas que coinciden con el criterio de búsqueda:\n")
            notas = gestor.buscar_nota(busqueda)
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "4":
            index = int(input("\n[\u270E] Introuce el índice de la nota que quieres borrar: "))
            gestor.eliminar_nota(index)

        elif  opcion == "5":
            break

        else:
            print("\n[!] La opción indicada es incorrecta.")

        input("\n Presiona Enter para continuar.")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()