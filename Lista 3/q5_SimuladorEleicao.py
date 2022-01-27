cand1, cand2, cand3 = 12, 13, 17
v1, v2, v3 = 0, 0, 0

qtd_eleitores = int(input("Digite a quantidade total de eleitores: "))

for i in range(qtd_eleitores):
    voto = int(input("Digite o número do seu candidato, só é válido digitar 12, 13 e 17: "))

    while (voto!=12 and voto!=13 and voto!=17):
        print("\n ---> NÚMERO DO CANDIDATO INEXISTENTE, POR FAVOR DIGITE NOVAMENTE: ")
        voto = int(input("Digite o número do seu candidato, só é válido digitar 12, 13 e 17: "))
    
    if voto==12:
        v1+=1

    elif voto==13:
        v2+=1

    else:
        v3+=1

print("\nO candidato de número %d recebeu %d voto(s)" %(cand1, v1))
print("O candidato de número %d recebeu %d voto(s)" %(cand2, v2))
print("O candidato de número %d recebeu %d voto(s)" %(cand3, v3))