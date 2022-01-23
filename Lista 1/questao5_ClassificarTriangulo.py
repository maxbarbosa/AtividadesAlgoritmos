lado1 = int(input("Digite o tamanho da base do triângulo: "))
lado2 = int(input("Digite o tamanho da lateral esquerda do triângulo: "))
lado3 = int(input("Digite o tamanho da lateral direita do triângulo: "))

if(lado1 == lado2 and lado2 == lado3):
    print("Triângulo Equilátero")
elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")