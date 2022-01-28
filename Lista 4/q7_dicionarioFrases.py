frase = str(input("Digite uma frase: "))

while (frase != "1"):
    dicionario = {}
    caracteres = frase.lower()
    for i in range(len(frase)):
        dicionario[frase[i]] = caracteres.count(caracteres[i])
    
    print(dicionario, "\n")
    frase = str(input("Digite uma frase: "))

print("\nPrograma encerrado!")