num = int(input("Digite um número para verificar se o mesmo é ou não é um número primo: "))

resto = 1
for i in range (2,num):
    if num%i == 0:
        resto = 0

if resto == 1:
    print("\nO número %d é um número primo." %(num))
else:
    print("\nO número %d NÃO é um número primo." %(num))