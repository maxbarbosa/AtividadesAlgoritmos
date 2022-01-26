total = 0
preco = 0
while (1):
    codigo = int(input("Digite o código do produto: "))

    if (codigo == 0):
        break

    qtd_comprada = int(input("Digite a quantidade de produtos: "))

    if codigo == 1:
        preco = 5.50
    elif codigo == 2:
        preco = 2.30
    elif codigo == 3:
        preco = 4.75
    elif codigo == 4:
        preco = 6.80
    elif codigo == 5:
        preco = 9.30
    else:
        print("Código inválido!")
    
    total+=preco*qtd_comprada
print("O valor total das compras é de R$ %.2f" %(total))