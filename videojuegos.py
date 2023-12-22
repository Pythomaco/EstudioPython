#!usr/bin/env python3

#-----variables-iniciales-----
juegos = ["Super Mario Bros",
          "Zelda: Breath of the Wild",
          "Cyberpunk 2077",
          "Final Fantasy VII"
          ]
ventas_minimas = int(input("Ventas mínimas: "))
ventas_totales = 0

#-----datos-----
generos = {
    "Super Mario Bros": "Plataformas",
    "Zelda: Breath of the Wild": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol"
}

ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breath of the Wild": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy VII": (924, 3)
}

clientes = {
    "Super Mario Bros": {"David", "Esteban", "Ryu", "Eli"},
    "Zelda: Breath of the Wild": {"Eli", "Julss", "Samu", "Ryu", "Dani"},
    "Cyberpunk 2077": {"Luisa", "Felipe", "Víctor", "Yoa"},
    "Final Fantasy VII": {"Dani", "David", "Ryu", "Felipe"}
}

#-----funciones-----
def sumario(juego):
    JUEGO = juego.upper()
    print(f"""
RESUMEN DEL JUEGO {JUEGO}:
    Género: {generos[juego]}
    Unidades vendidas: {ventas_y_stock[juego][0]}
    Unidades en stock: {ventas_y_stock[juego][1]}
    Compradores: {', '.join(clientes[juego])}

""")
    
#-----acciones-----
for juego in juegos:
    if ventas_y_stock[juego][0] >= ventas_minimas:
        ventas_totales += ventas_y_stock[juego][0]
        sumario(juego)

print(f"Total de unidades vendidas: {ventas_totales}")