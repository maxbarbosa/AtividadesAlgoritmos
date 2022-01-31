def imprimirEscadaNumeros(numero):
    for i in range(1, numero+1):
        linha = ""
        for j in range(i):
            linha += str(i) + " "
        print(linha)

n = int(input("Digite um número inteiro positivo: "))

while n<=0 :
    print("\033[1;33m", "\nO número precisa ser maior que 0.", "\033[0m")
    n = int(input("Digite um número inteiro positivo: "))

imprimirEscadaNumeros(n)