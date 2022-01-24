i=1
soma = 0
while (i<=500):
    if (i%2 != 0 and i%3 == 0):
        soma += i
    i+=1
print("A soma de todos os números ímpares e multiplos de três no intervalo de 1 à 500 é de: %d" %(soma))