from random import randint
n = int(input("Digite quantas vezes o dado será lançado: "))

while (n != 0):

    while (n < 0):
        print("\n" + "*"*50 + "\n")
        print("O número de lançamentos não pode ser negativo!")
        n = int(input("Digite quantas vezes o dado será lançado: "))
        print("\n" + "*"*50 + "\n")

    faces = []
    numeros = [0,0,0,0,0,0]
    
    if n == 0:
        break

    for i in range(n):
        
        x = randint(1,6)
        faces.append(x)
    
        numeros[x-1]+=1
    
    print("\n" + "*"*50 + "\n")
    
    for i in range(6):
        print("O número %d apareceu em %.2f%% dos lançamentos." %(i+1, numeros[i]/len(faces)*100))
    
    print("\n" + "*"*50 + "\n")

    n = int(input("Digite quantas vezes o dado será lançado: "))

print("\nPrograma encerrado!")