inventario = 1000

while inventario > 0:
    print(f"Vacunas disponibles hoy: {inventario}")
    entregas = int(input("Ingrese la cantidad de vacunas entregadas hoy: "))
    inventario -= entregas

    if inventario < 200:
        print("¡Alerta! El inventario de vacunas ha bajado de 200 unidades.")

print("El inventario de vacunas ha llegado a cero. Se ha agotado el stock.")