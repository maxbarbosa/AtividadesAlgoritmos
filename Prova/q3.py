texto = str(input("Digite uma frase qualquer: "))
char_1 = texto[0]
texto_mod = ""

for i in range(len(texto)):
    if texto[i] == char_1:
        texto_mod += "#"
    else:
        texto_mod += texto[i]

print("Texto original: %s" %(texto))
print("Texto modificado: %s" %(texto_mod))