n1 = int(input("Digite o valor do primeiro número: "))
n2 = int(input("Digite o valor do segundo número: "))
a1 = n1

subtracoes_possiveis = 0
while (n1>=n2):
    subtracoes_possiveis+=1
    n1 = n1-n2

print("\nA divisão inteira de %d por %d é igual a: %d"% (a1, n2, subtracoes_possiveis))
print("O resto da divisão de %d por %d é igual a: %d"% (a1, n2, n1))
print("Podemos subtrair o valor %d '%d' vezes de %d" %(n2, subtracoes_possiveis, a1))