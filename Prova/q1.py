lista_a = []
lista_b = []

print("Digite 10 números!")
for i in range(10):
    num = int(input("Digite o %dº número: "%(i+1)))
    lista_a.append(num)

for j in range(10):
    lista_b.append(lista_a[j]**2)

    print("A[%d] = %d B[%d] = %d" %(j+1, lista_a[j], j+1, lista_b[j]))