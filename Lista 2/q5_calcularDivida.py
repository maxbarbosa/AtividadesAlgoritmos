valor_divida  = float(input("Digite o valor da dívida: "))
juros_mensais = float(input("Digite a taxa de juros mensais: "))
valor_pagamento = float(input("Digite o valor mensal do pagamento: "))

meses = 0
total_pago = valor_divida
juros_pago = 0
if (valor_divida*juros_mensais/100 >= valor_pagamento):
    print("\nA dívida nunca terá fim, pois o valor do pagamento mensal é inferior a taxa de juros!")
else:
    while(valor_divida >= valor_pagamento):
        juros = valor_divida * juros_mensais/100
        valor_divida += juros-valor_pagamento
        juros_pago += juros
        meses+=1

    total_pago += juros_pago
    print("\nSerão necessários %d meses para pagar a dívida."%(meses))
    print("Total de juros pago: R$ %.2f" %(juros_pago))
    print("Total pago: R$ %.2f" %(total_pago))