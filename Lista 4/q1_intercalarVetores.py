lista1, lista2, lista3 = [], [], []

for i in range(5):
    n1 = int(input("Digite um número inteiro para LISTA-1 [%d]: "%(i+1)))
    lista1.append(n1)

print('-'*100)
for i in range(5):
    n2 = int(input("Digite um número inteiro para LISTA-2 [%d]: "%(i+1)))
    lista2.append(n2)

    lista3.append(lista1[i])
    lista3.append(lista2[i])

print("\nLista com os elementos intercalados das listas 1 e 2:\n\n", lista3)