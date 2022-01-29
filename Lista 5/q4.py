texto_original = str(input("Digite uma frase: "))
frase_sem_espaco = ""

while len(texto_original) == 0:
    print("\033[1;33m", "A quantidade mínima de caracteres é 1.", "\033[0m",)
    texto_original = str(input("Digite uma frase: "))

for i in range(len(texto_original)):
    caractere = texto_original[i]
    if caractere != " ":
        frase_sem_espaco+=caractere

print("\nTexto original  : %s" %(texto_original))
print("Texto sem espaço: %s" %(frase_sem_espaco))