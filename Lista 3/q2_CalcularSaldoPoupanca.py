deposito_inicial = float(input("Digite o valor do depósito inicial na sua conta poupança: "))
juros = float(input("Digite a taxa de juros mensais, Exemplo: caso seja (0,7%) ao mês digite 0.7: "))/100

for t in range(1, 25):
    montante = deposito_inicial*(1+juros)**t
    print("Saldo parcial da conta ao final do %dº mês é de R$ %.2f" %(t, montante))

print("\nO total ganho com juros no período de 24 meses foi de R$ %.2f" %(montante-deposito_inicial))
print("O saldo da conta após 24 meses é de R$ %.2f" %(montante))