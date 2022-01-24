valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = str(input("Informe qual a forma de pagamento! Digite 'dinheiro' ou 'cheque': "))

if (valor_produto >= 100 and forma_pagamento == "dinheiro"):
    valor_pagamento = valor_produto-(valor_produto*0.10)
    print("R$ %.2f" %(valor_pagamento))

elif(forma_pagamento != "dinheiro" and forma_pagamento != "cheque"):
    print("Forma de pagamento inválida")

else:
    print("R$ %.2f" %(valor_produto))