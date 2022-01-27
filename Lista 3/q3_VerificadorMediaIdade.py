qtd_pessoas = int(input("Digite a quantidade de pessoas: "))

somador = 0
for i in range(qtd_pessoas):
    idade = int(input("Digite sua idade: "))

    somador += idade

media_idade = somador/qtd_pessoas

if media_idade <= 25:
    print("\nA idade média da turma é de %.1f anos.\nA turma é jovem." %(media_idade))
elif media_idade <= 60:
    print("\nA idade média da turma é de %.1f anos.\nA turma é adulta." %(media_idade))
else:
    print("\nA idade média da turma é de %.1f anos.\nA turma é idosa." %(media_idade))