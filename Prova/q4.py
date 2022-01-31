def calcularPotencia(base, expoente):
    soma = base

    resultado = 1

    if expoente < 0:
        expoente = -(expoente)
        for i in range(expoente):
                resultado *= soma
        
        return ("\n%d elevado ao expoente -%d resulta em %.15f" %(base, expoente, 1/resultado))

    else:
        for i in range(expoente):
            resultado *= soma

        return ("\n%d elevado ao expoente %d resulta em %d" %(base, expoente, resultado))

b = int(input("Digite um valor inteiro para a base: "))
e = int(input("Digite um valor inteiro para o expoente: "))

exibir_resultado = calcularPotencia(b, e)
print(exibir_resultado)