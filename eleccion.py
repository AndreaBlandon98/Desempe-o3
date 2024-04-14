candidatos = ["Candidato A", "Candidato B", "Candidato C"]
votos = [0, 0, 0]
for i in range(200):
    voto = int(input(f"Ingrese el número del candidato elegido por el elector {i+1} (1, 2 o 3): "))
    votos[voto-1] += 1
indice_ganador = votos.index(max(votos))
ganador = candidatos[indice_ganador]
print(f"El ganador de las elecciones es: {ganador} con {votos[indice_ganador]} votos.")

