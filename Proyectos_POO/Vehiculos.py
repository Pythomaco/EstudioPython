#!usr/bin/env python3

class Vehiculo:

    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def __str__(self):
        return f"· Vehículo {self.modelo} ({self.matricula}): {"disponible" if self.disponible else "no disponible"}"

    def alquilar(self):
        if self.disponible == True:
            self.disponible = False
        else:
            print(f"[!] Vehículo con matrícula {self.matricula} no está disponible.")

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
        else:
            print(f"[!] Vehículo con matrícula {self.matricula} no está alquilado.")


class Flota:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

if __name__ == "__main__":

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("5384FGH", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("8945LWX", "Honda Civic"))

    print(f"""[*] Flota inicial:
          """)
    print(flota)

    flota.alquilar_vehiculo("5384FGH")
    print("""
          """)
    print(f"""[*] Flota después:
          """)
    
    print(flota)

    flota.devolver_vehiculo("8945LWX")