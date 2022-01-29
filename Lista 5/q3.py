def validarCPF(cpf):
    cpf_apenas_numeros = ""
    soma_digito1 = 0
    soma_digito2 = 0
    digito1 = 0
    digito2 = 0

    for i in range(len(cpf)):
        if cpf[i] > "9":
            return "\033[1;31m" + "\nO CPF informado é inválido. Deve conter apenas números, 1 hífen e 2 pontos." + "\033[0m"

        if cpf[i] != "." and cpf[i] != "-":
            
            cpf_apenas_numeros+=cpf[i]

    primeiro = cpf_apenas_numeros[0]
    iguais = True
    for i in range(11):
        if primeiro != cpf_apenas_numeros[i]:
            iguais = False
    
    if iguais:
        return "\033[1;31m" + "\nO CPF informado é inválido. Todos os digítos são iguais." + "\033[1;31m"

    for i in range(10, 1, -1):
        soma_digito1 += int(cpf_apenas_numeros[10-i])*i

    for i in range(11, 1, -1):
        soma_digito2 += int(cpf_apenas_numeros[11-i])*i

    if soma_digito1%11 >= 2:
        digito1 = 11 - soma_digito1%11

    if soma_digito2%11 >= 2:
        digito2 = 11 - soma_digito2%11

    if digito1 == int(cpf[12]) and digito2 == int(cpf[13]):
        return "\033[1;32m" + "\nO CPF informado é válido." + "\033[0m"
    
    else:
        return "\033[1;31m" + "\nO CPF informado é inválido." + "\033[0m"

cpf_1 = str(input("Digite um CPF para testar se o mesmo é válido, no formato XXX.XXX.XXX-XX: "))

while len(cpf_1) != 14 or cpf_1[3] != "." or cpf_1[7] != "." or cpf_1[11] != "-":
    print("\033[1;33m", "O formato do CPF é inválido!", "\033[0m")
    cpf_1 = str(input("Digite um CPF para testar se o mesmo é válido, no formato XXX.XXX.XXX-XX: "))

print(validarCPF(cpf_1))