string1 = str(input("Digite uma primeira frase qualquer: "))
string2 = str(input("Digite uma segunda frase qualquer: "))

while (len(string1) ==0) or (len(string2) ==0):
    print("\033[1;33m", "NENHUMA FRASE PODE FICAR VAZIA!", "\033[0m")
    
    if (len(string1) == 0) and (len(string2) == 0):
        string1 = str(input("Digite uma primeira frase qualquer: "))
        string2 = str(input("Digite uma segunda frase qualquer: "))

    elif len(string1) == 0:
        string1 = str(input("Digite uma primeira frase qualquer: "))
    
    else:
        string2 = str(input("Digite uma segunda frase qualquer: "))

print("\nConteúdo da primeira frase: %s \nQuantidade de caracteres: %d" %(string1, len(string1)))
print("*"*50)
print("Conteúdo da segunda frase: %s \nQuantidade de caracteres: %d" %(string2, len(string2)))

if len(string1) == len(string2):
    print("\033[1;32m", "\nAmbas frases tem a mesma quantidade de caracteres.", "\033[0m")
else:
    print("\033[1;31m", "\nAs frases não possuem a mesma quantidade de caracteres.", "\033[0m")

if string1 == string2:
    print("\033[1;32m", "\nAmbas frases possuem o mesmo conteúdo.", "\033[0m")
else:
    print("\033[1;31m", "\nAs frases possuem conteúdos diferentes.", "\033[0m")