def actualizar_precio(precio_anterior, inflacion_mensual):
    precio_actualizado = precio_anterior * (1 + inflacion_mensual)
    return precio_actualizado

precio_anterior = float(input("Ingrese el precio anterior de la planta: "))
inflacion_mensual = float(input("Ingrese el valor de la inflación mensual: "))

precio_actualizado = actualizar_precio(precio_anterior, inflacion_mensual)
print(f"El precio actualizado de la planta es: {precio_actualizado}")
