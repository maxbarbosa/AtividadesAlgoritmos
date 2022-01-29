def verificadorDatas(data):
    global dia, mes, ano
    dia = ''
    mes = ''
    ano = ''

    for i in range(2):
        dia+=data[i]

    for j in range(3, 5):
        mes+=data[j]

    for k in range(6, 10):
        ano+= data[k]
        
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
data_nascimento = str(input("Digite a sua data de nascimento no formato DD/MM/AAAA: "))

while (len(data_nascimento) != 10) or (data_nascimento[2] != '/') or (data_nascimento[5] != '/'):
    print("\033[1;33m", "\nData inválida!", "\033[0m")
    data_nascimento = str(input("\nDigite a sua data de nascimento no formato DD/MM/AAAA: "))

verificadorDatas(data_nascimento)

#DEFININDO UM LIMITE INFERIOR E SUPERIOR PARA O ANO DE NASCIMENTO
while (dia<1) or (dia>31) or (mes<1) or (mes>12) or (ano<1910) or (ano>2021):        
    print("\033[1;33m", "\nData inválida!", "\033[0m")
    
    data_nascimento = str(input("\nDigite a sua data de nascimento no formato DD/MM/AAAA: "))
    verificadorDatas(data_nascimento)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

m = lista_meses[mes-1]

print("Data por extenso: %d de %s de %d." %(dia, m, ano))