texto = str(input("Digite uma palavra ou frase qualquer: ")).rstrip()

while len(texto) == 0:
    print("\033[1;33m", "O conteúdo da palavra/frase não pode ser vazio!", "\033[0m")
    texto = str(input("Digite uma palavra ou frase qualquer: "))

saida = ""
for i in range(len(texto)):
    saida += texto[i]
    print(saida)