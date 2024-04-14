salarios = []

def calcular_salario_con_incremento(salario):
    salario_incrementado = salario * 1.025  # Incremento del 2.5%
    return salario_incrementado

for i in range(1, 21):
    salario = float(input(f"Ingrese el salario del empleado {i} por mes: "))
    salarios.append(salario)

promedio_salarios = sum(salarios) / len(salarios)

print(f"\nEl promedio de los salarios es: ${promedio_salarios:.2f}\n")

print("Salario de cada empleado con un incremento del 2.5%:")
for i, salario in enumerate(salarios):
    nuevo_salario = calcular_salario_con_incremento(salario)
    print(f"Empleado {i+1}: ${nuevo_salario:.2f}")
print("Salario de cada empleado con un incremento del 2.5%:")
for i, salario in enumerate(salarios):
    nuevo_salario = calcular_salario_con_incremento(salario)
    print(f"Empleado {i+1}: ${nuevo_salario:.2f}")
print("Salario de cada empleado con un incremento del 2.5%:")
for i, salario in enumerate(salarios):
    nuevo_salario = calcular_salario_con_incremento(salario)
    print(f"Empleado {i+1}: ${nuevo_salario:.2f}")
