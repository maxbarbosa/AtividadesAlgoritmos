from random import randint

arquivo = "q8.txt"
lista_palavras = []
with open(arquivo, mode = "r", encoding= "utf-8") as arq:
    for linha in arq:
        palavra = linha.rstrip().upper()
        lista_palavras.append(palavra)
arq.close()

palavra_aleatoria = lista_palavras[randint(0, len(lista_palavras)-1)]

sublinhado = ['_']*len(palavra_aleatoria)
letras_usadas = []
letras_acertadas = []

print("*"*18 + "\n* JOGO DA FORCA  *\n" + "*"*18 + "\n")

erros = 0
acertos = 0

vermelho = "\033[1;31m"
verde = "\033[1;32m"
amarelo = "\033[1;33m"
resetar_cor = "\033[0m"

while erros < 6:

    print("\nA palavra é: ", end = "")
    for i in range(len(palavra_aleatoria)):
        print(sublinhado[i], end= " ")

    letra = str(input("\n\nDigite uma letra: ")).upper()

    while len(letra) == 0:
        print(amarelo, "\n---> A letra não pode ser vazia!", resetar_cor)
        letra = str(input("Digite uma letra: ")).upper()

    #OBS: para essa questão resolvi admitir apenas os caracteres de A-Z e cedilha (sem acentuação).
    #verificando se a entrada não é uma letra com base nos valores da tabela ASCII.
    while len(letra) > 1 or letra < "A" or letra > "Z" and letra != "Ç":
        print(amarelo, "---> O caractere informado não é uma letra!", resetar_cor)
        letra = str(input("\n\nDigite uma letra: ")).upper()
    
    while letra in letras_usadas:
        print(amarelo, "\n---> Você já usou essa letra, tente outra distinta!", resetar_cor)
        letra = str(input("Digite uma letra: ")).upper()

    if letra not in letras_usadas:
        letras_usadas.append(letra)

    
    if letra not in palavra_aleatoria:
        erros+=1
        aviso = "\n---> Você errou pela %dª vez. Tente novamente!" %(erros)
        
        if erros == 6:
            aviso = "\n---> Você errou pela %dª vez." %(erros)

        print(amarelo, "%s" %(aviso), resetar_cor)

        if erros == 5:
            print(amarelo, "\n---> AVISO: Se errar mais uma vez será enforcado! <---", resetar_cor)
    
    else:
        for i in range(len(palavra_aleatoria)):
            if letra == palavra_aleatoria[i] and letra not in letras_acertadas:
                sublinhado[i] = letra
                acertos+=1
    
        letras_acertadas.append(letra)

    if erros == 6:
        print("\nA palavra era: ", end = "")
        for i in range(len(palavra_aleatoria)):
            print(palavra_aleatoria[i], end= " ")
        
        print(vermelho, "\n\nGAME OVER! Você perdeu.", resetar_cor)

    if acertos == len(palavra_aleatoria):
        print("\nA palavra era: ", end = "")
        for i in range(len(palavra_aleatoria)):
            print(palavra_aleatoria[i], end= " ")

        print(verde, "\n\nCONGRATULATIONS! Você venceu.", resetar_cor)
        break