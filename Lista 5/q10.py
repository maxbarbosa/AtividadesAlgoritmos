def is_PositivoNegativo(numero):
    status = ''
    if numero <= 0:
        status = "\033[1;31m" + "N" + "\033[0m"
    else:
        status = "\033[1;32m" + "P" + "\033[0m"

    return status

n = int(input("Digite um número inteiro para verificar se ele é negativo ou positivo: "))
verificarPosNeg = is_PositivoNegativo(n)
print("O número %d é %s" %(n, verificarPosNeg))