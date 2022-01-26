n = int(input("Digite o valor que deseja saber a raiz quadrada: "))
b = 2
p = (b+n/b)/2
while(0.0001 < abs(b-p)):
    b = p
    p = (b+n/b)/2

print("A raiz quadrada de %d é: %.2f" %(n, b))