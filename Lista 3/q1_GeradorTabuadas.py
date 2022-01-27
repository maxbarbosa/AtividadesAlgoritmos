num = int(input("Digite um número o qual você deseja ver a tabuada de 1 a 10: "))

while num<1 or num>10:
    num = int(input("O número %d não está no intervalo de 1 a 10, digite um número dentro do intervalo: " %(num)))

print("\nTabuada de %d:\n"%(num))
for i in range(1,11):
    print("%d x %d = %d" %(num, i, num*i))