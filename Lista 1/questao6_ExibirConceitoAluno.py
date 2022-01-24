nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1+nota2)/2

if (media > 9):
    conceito = 'A'
elif (media >= 7.5):
    conceito = 'B'
elif (media >= 6):
    conceito = 'C'
elif (media >= 4):
    conceito = 'D'
else:
    conceito = 'E'
print("O conceito semestral do aluno é '%s'."%(conceito))