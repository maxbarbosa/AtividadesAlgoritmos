soma = base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = 1

if expoente < 0:
    expoente = -(expoente)
    for i in range(expoente):
            resultado *= soma
    
    print("\n%d elevado ao expoente -%d resulta em %.15f" %(base, expoente, 1/resultado))

else:
    for i in range(expoente):
        resultado *= soma

    print("\n%d elevado ao expoente %d resulta em %d" %(base, expoente, resultado))