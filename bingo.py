import random
numeros_bingo = list(range(1, 76))
def sacar_numero():
    numero = random.choice(numeros_bingo)
    numeros_bingo.remove(numero)
    return numero
def imprimir_carton(carton):
    for fila in carton:
        print(fila)
carton = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            carton[i][j] = "X"
        else:
            numero = sacar_numero()
            carton[i][j] = numero
print("¡Bienvenido al Bingo Digital!")
print("Tu cartón de bingo es:")
imprimir_carton(carton)

while True:
    input("Presiona Enter para sacar un número:")
    numero_sacado = sacar_numero()
    print(f"Número sacado: {numero_sacado}")

    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero_sacado:
                carton[i][j] = "X"
                print("¡Tienes ese número en tu cartón!")
        imprimir_carton(carton)

    continuar = input("¿Quieres seguir jugando? (s/n): ")
    if continuar.lower() != "s":
        break

print("¡Gracias por jugar al Bingo Digital!")
