precio_agua = 3.5  # Precio por metro cúbico
precio_luz = 0.25   # Precio por kilovatio hora
precio_gas = 1.2    # Precio por metro cúbico

def calcular_pago_mensual(consumo_agua, consumo_luz, consumo_gas):
    pago_agua = consumo_agua * precio_agua
    pago_luz = consumo_luz * precio_luz
    pago_gas = consumo_gas * precio_gas
    pago_total = pago_agua + pago_luz + pago_gas
    return pago_total, pago_agua, pago_luz, pago_gas

consumo_agua_mensual = float(input("Ingrese el consumo de agua del mes (metros cúbicos): "))
consumo_luz_mensual = float(input("Ingrese el consumo de luz del mes (kilovatio horas): "))
consumo_gas_mensual = float(input("Ingrese el consumo de gas del mes (metros cúbicos): "))

pago_total_mensual, pago_agua_mensual, pago_luz_mensual, pago_gas_mensual = calcular_pago_mensual(consumo_agua_mensual, consumo_luz_mensual, consumo_gas_mensual)

print(f"Para el mes actual:")
print(f"El total a pagar es: ${pago_total_mensual:.2f}")
print(f"Desglose del pago:")
print(f"Agua: ${pago_agua_mensual:.2f}")
print(f"Luz: ${pago_luz_mensual:.2f}")
print(f"Gas: ${pago_gas_mensual:.2f}")

consumo_agua_anual = consumo_agua_mensual * 12
consumo_luz_anual = consumo_luz_mensual * 12
consumo_gas_anual = consumo_gas_mensual * 12

pago_total_anual, _, _, _ = calcular_pago_mensual(consumo_agua_anual, consumo_luz_anual, consumo_gas_anual)

print(f"\nPara todo el año:")
print(f"El total a pagar es: ${pago_total_anual:.2f}")
