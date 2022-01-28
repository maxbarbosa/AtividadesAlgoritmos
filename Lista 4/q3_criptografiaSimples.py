print("Intervalo da sequência: 0 até 26")
entrada = True
alfabeto= " abcdefghijklmnopqrstuvwxyz"
mensagem = ''

while entrada:

    sequencia = input("Digite uma sequência de números inteiros separados por espaço: ").split()
    invalido = False

    for j in range(len(sequencia)):

        numero = int(sequencia[j])

        if numero<0 or numero>26:
            print("Sequência inválida, algum número está fora do intervalo [0,26].")
            invalido = True
            break
    
    entrada = invalido
    
for i in range(len(sequencia)):
    
    letra = int(sequencia[i])
    mensagem+=alfabeto[letra]

print("\nA sequência: ")
for e in sequencia:
    print(e, end= " -> ")

print("\nTem por tradução a seguinte mensagem: '%s'" %(mensagem))