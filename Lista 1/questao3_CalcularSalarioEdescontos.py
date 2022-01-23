ganho_por_hora = float(input("Digite o valor que você recebe por hora: "))
horas_mensais = int(input("Digite o número de horas trabalhadas por mês: "))

salario_bruto = horas_mensais*ganho_por_hora
imposto_renda = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-imposto_renda-inss-sindicato

print("Salário Bruto: R$ %.2f \nIR(11%%): R$ %.2f \nINSS(8%%): R$ %.2f \nSindicato(5%%): R$ %.2f \nSalário Líquido: R$ %.2f" %(salario_bruto, imposto_renda, inss, sindicato, salario_liquido))