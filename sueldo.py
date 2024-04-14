def calcular_sueldo_promedio(lista_sueldos):
    total_sueldos = sum(lista_sueldos)
    sueldo_promedio = total_sueldos / len(lista_sueldos)
    return sueldo_promedio

empleados = int(input("Ingrese la cantidad de empleados: "))
lista_sueldos = []

for i in range(empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    lista_sueldos.append(sueldo)

promedio = calcular_sueldo_promedio(lista_sueldos)
print(f"El sueldo promedio del grupo de empleados es: {promedio}")

