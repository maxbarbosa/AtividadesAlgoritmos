altura = float(input("Digite a altura em centímetros com até 2 casas decimais: "))
sexo = str(input("Digite 'F' para feminino ou 'M' para masculino: "))

if sexo == 'F':
	print("O peso ideal com base em %.2fcm de altura para mulheres é de %.2fkg."%(altura,(62.1*altura)-44.7))
elif sexo == 'M':
	print("O peso ideal com base em %.2fcm de altura para homens é de %.2fkg."%(altura,(72.7*altura)-58))
else:
	print("Opção de sexo inválida, execute o programa novamente.")
