qtd_votos = [0,0,0,0,0,0]

votos = 1
vencedor = 6

print("Lista das opções de voto: ")
print("1 - Java\n2 - Python\n3 - R\n4 - C++\n5 - Julia\n6 - Outro\n")

for i in range(500):
    voto = int(input("Digite um número entre 1 e 6 para representar seu voto: "))
    
    while voto < 1 or voto > 6:
        voto = int(input("Opção inválida, digite novamente entre [1, 6]: "))
        
    qtd_votos[voto-1]+=1

for i in range(6):
    print("\nA opção %d obteve %.2f%% dos votos" %(i+1, qtd_votos[i]/6*100))


for i in range(6):
    if qtd_votos[i] > votos:
        votos = qtd_votos[i]
        vencedor = i

print()

if vencedor == 0:
    print("1 - Java venceu a enquete.")
elif vencedor == 1:
    print("2 - Python venceu a enquete.")
elif vencedor == 2:
    print("3 - R venceu a enquete.")
elif vencedor == 3:
    print("4- C++ venceu a enquete.")
elif vencedor == 4:
    print("5 - Julia venceu a enquete.")
elif vencedor == 5:
    print("6 - Outro venceu a enquete.")
else:
    print("Houve empate na enquete")
