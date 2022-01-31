def somarTresNumeros(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma

n1 = int(input("Digite o valor do 1º número: "))
n2 = int(input("Digite o valor do 2º número: "))
n3 = int(input("Digite o valor do 3º número: "))

resultado_soma = somarTresNumeros(n1, n2, n3)

print("O resultado da soma de %d + %d + %d é igual a %d" %(n1, n2, n3, resultado_soma))