notas = []

while True:
    nota = int(input('digite uma nota ou -1 pra sair: '))
    if nota == -1:
        break

    notas.append(nota)

print(notas)
