from math import sqrt
distMinima = 999999999
distMaxima = 0
distMedia = 0
soma_distancia = 0
pontos = []

n = int(input("Digite a quantidade de pontos: "))

while ( n<2 ):
    print("A quantidade de pontos precisa ser no mínimo 2!!!")
    n = int(input("Digite a quantidade de pontos: "))
    print("\n" + "*"*50 + "\n")

for i in range(n):
    x, y = input("Digite as coordenadas X, Y do ponto P%d separadas por um espaço: "%(i+1)).split()
    coords = (int(x), int(y))
    pontos.append(coords)

comparacoes = 0
for i in range (n):
    for j in range (i+1,n):
        distancia = sqrt((pontos[j][0]-pontos[i][0])**2 + (pontos[j][1]-pontos[i][1])**2)
        soma_distancia+=distancia
        
        if distancia > distMaxima:
            distMaxima = distancia
        
        if distancia < distMinima:
            distMinima = distancia
        
        comparacoes+=1
distMedia = soma_distancia/comparacoes

print("\nDistância mínima: %.2f" %(distMinima))
print("Distância máxima: %.2f" %(distMaxima))
print("Distância média: %.2f" %(distMedia))