valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = str(input("Informe qual a forma de pagamento! Digite 'dinheiro', 'cheque' ou 'cartão': "))

if (valor_produto >= 100 and forma_pagamento == "dinheiro"):
    valor_pagamento = valor_produto-(valor_produto*0.10)
    print("R$ %.2f" %(valor_pagamento))

elif (valor_produto < 100 and forma_pagamento == "dinheiro"):
    print("R$ %.2f" %(valor_produto))

elif (forma_pagamento == "cartão"):
    funcao_cartao = str(input("Informe qual a função do cartão! Digite 'crédito' ou 'débito': "))
    
    if(funcao_cartao == "crédito"):
        qtd_parcelas = int(input("Dividimos em até TRÊS vezes. Digite o número de parcelas de 1 a 3: "))
        if (qtd_parcelas<=3):
            print("R$ %.2f\n%d parcelas de R$ %.2f" %(valor_produto, qtd_parcelas, valor_produto/qtd_parcelas))
        else:
            print("Quantidade de parcelas inválida")
    else:
        print("R$ %.2f" %(valor_produto))

elif (forma_pagamento == "cheque"):
    print("R$ %.2f" %(valor_produto))

else:
    print("Forma de pagamento inválida")