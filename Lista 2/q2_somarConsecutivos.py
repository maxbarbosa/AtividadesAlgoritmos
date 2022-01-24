n = int(input("Digite um valor inteiro: "))
soma = n
maior = n
menor = n
while (n != -1):
    n = int(input("Digite um valor inteiro: "))

    if n == -1:
        break

    if (n > maior):
        maior = n
    if (n < menor):
        menor = n

    soma+=n
print("O menor valor digitado foi: %d" %(menor))
print("O maior valor digitado foi: %d" %(maior))
print("A soma de todos valores digitados é: %d"%(soma))