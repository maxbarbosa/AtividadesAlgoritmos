def verificarQtdDigitos(numero):
    qtd_digitos = 0 
    if numero < 0:
        qtd_digitos = len(str(numero))-1
    else:
        qtd_digitos = len(str(numero))

    return qtd_digitos
    
n = int(input("Digite um número inteiro qualquer: "))

exibirNaTela = verificarQtdDigitos(n)
print("O número %d possui %d dígito(s)." %(n, exibirNaTela))