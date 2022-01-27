n = int(input("Digite a quantidade de elementos da sequência Fibonacci você deseja visualizar: "))

aux1 = 1 

for i in range(n):
    if i<2 or n<=2:
        aux2 = aux1
        print(aux2, end = " ")
    else:
        aux3 = aux1+aux2
        print(aux3, end = " ")
        aux1 = aux2
        aux2 = aux3