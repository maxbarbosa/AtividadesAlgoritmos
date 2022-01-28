matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um valor inteiro para matriz[%d][%d]: "%(i+1, j+1)))
        linha.append(n)
    matriz.append(linha)

print("\nMatriz original:\n")
for l in matriz:
    print(l)

linha2 = []
coluna2 = []
for k in range(3):
    linha2.append(matriz[1][k])
    coluna2.append(matriz[k][1])
    matriz[k][1] = linha2[k]
    matriz[1][k] = coluna2[k]

print("\nMatriz após trocar a 2ª linha pela 2ª coluna:\n")
for l in matriz:
    print(l)