altura = []
sexo = []

menor, maior = 100, 0
Smin = Smax = ""
qtdF = qtdM = 0
alturasF = mediaF = alturasM = mediaM = 0
#um limite inferior pra altura foi definido, pois nem mesmo bebês prematuros nascem com menos de 40cm
for i in range(10):

    a = float(input("Digite a altura da %dª pessoa:      "%(i+1)))
    while (a < 0.40):
        print("A altura não pode ser inferior a 0.40cm")
        a = float(input("Digite a altura da %dª pessoa:      "%(i+1)))

    s = input("Informe o sexo 'M/F' da %dª pessoa: "%(i+1)).upper()
    while (s != 'M' and s != 'F'):
        print("O sexo só pode ser M ou F.")
        s = input("Informe o sexo 'M/F' da %dª pessoa: "%(i+1)).upper()
    
    altura.append(a)
    sexo.append(s)

    if altura[i] > maior:
        maior = altura[i]
        Smax = sexo[i]
    
    if altura[i] < menor:
        menor = altura[i]
        Smin = sexo[i]

    if sexo[i] == "F":
        qtdF+=1
        alturasF+=altura[i]
    
    else:
        qtdM+=1
        alturasM+=altura[i]

if (qtdF>0):
    mediaF = alturasF/qtdF

if (qtdM>0):
    mediaM = alturasM/qtdM

print("\nA pessoa de maior altura possui %.2fcm e é do sexo %s." %(maior, Smax))
print("A pessoa de menor altura possui %.2fcm e é do sexo %s."%(menor, Smin))
print('-'*100)
print("A média de altura das pessoas do sexo feminino é de %.2fcm." %(mediaF))
print("A média de altura das pessoas do sexo masculino é de %.2fcm." %(mediaM))
print('-'*100)
print("Quantidade de pessoas do sexo feminino: %d"%(qtdF))
print("Quantidade de pessoas do sexo masculino: %d"%(qtdM))