def contar_vocales_consonantes(letras):
    vocales = 0
    consonantes = 0
    for letra in letras:
        if letra.lower() in 'aeiou':
            vocales += 1
        elif letra.isalpha():
            consonantes += 1
    return vocales, consonantes

letras = []
for i in range(10):
    letra = input(f"Ingrese la letra {i+1}: ")
    letras.append(letra)

vocales, consonantes = contar_vocales_consonantes(letras)
print(f"Se ingresaron {vocales} vocales y {consonantes} consonantes.")
