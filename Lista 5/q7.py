def escreverPorExtenso(numero):
    numero_por_extenso = ""

    unidade = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    casa_dez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if numero <= 9:
        numero_por_extenso = unidade[numero-1]
    
    elif numero <= 19:
        numero = str(numero)
        numero_por_extenso = casa_dez[int(numero[1])]
    
    else:
        numero = str(numero)
        numero_por_extenso = dezenas[int(numero[0])-2]
        
        if numero[1] != '0':
            numero_por_extenso += " e " + unidade[int(numero[1])-1] 

    return numero_por_extenso

n = int(input("Digite um número inteiro de 1 a 99: "))

while n<1 or n>99:
    print("\033[1;31m", "O NÚMERO DIGITADO NÃO ESTÁ NO INTERVALO [1, 99].", "\033[0m")
    n = int(input("Digite um número inteiro de 1 a 99: "))

exibirNaTela = escreverPorExtenso(n)

print("\nNúmero inteiro: %d\nNúmero inteiro por extenso: %s" %(n, exibirNaTela))