def contadorCaracteres(frase):
    dicionario = {}

    for i in range(len(frase)):
        letra = frase[i]
        qtd_letra = 1
        
        for j in range(i+1, len(frase)):
            prox_letra = frase[j]
            
            if letra == prox_letra:
                qtd_letra+=1

        if letra not in dicionario.keys():
            dicionario[letra] = qtd_letra

    return dicionario

entrada = str(input("Digite uma frase qualquer: "))

while len(entrada) == 0:
    print("\033[1;33m", "A frase não pode ficar vazia.", "\033[0m")
    entrada = str(input("Digite uma frase qualquer: "))

print(contadorCaracteres(entrada))