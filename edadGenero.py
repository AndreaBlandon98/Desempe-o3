def calcular_promedio(lista_edades):
    total_edades = sum(lista_edades)
    promedio = total_edades / len(lista_edades)
    return promedio
edades_hombres = [25, 30, 22, 28, 26]
edades_mujeres = [27, 29, 24, 26, 28]

promedio_hombres = calcular_promedio(edades_hombres)
promedio_mujeres = calcular_promedio(edades_mujeres)

print(f"El promedio de edad de hombres es: {promedio_hombres} años")
print(f"El promedio de edad de mujeres es: {promedio_mujeres} años")
