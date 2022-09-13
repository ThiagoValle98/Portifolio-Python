preco = float(input('Digite o valor do produto: '))
pag = str(input('Digite a forma de pagamento? Sendo [D] para dinheiro, [K], para cheque, [C] para cartão,')).strip().upper()
parcelamento = int(input('Deseja pagar em quantas vezes? '))
if pag == "D" or pag == "K":
    preco = preco * 0.90
    print('O valor a ser paho é de {} Reais'.format(preco))
elif pag == "C" and parcelamento == 1:
    preco = preco * 0.95
    print('O valor a ser paho é de {} Reais'.format(preco))
elif pag == "C" and parcelamento == 2:
    print('O valor a ser paho é de {} Reais'.format(preco))
elif pag == "C" and parcelamento >= 3:
    preco= preco * 1.20
    print('O valor a ser paho é de {} Reais'.format(preco))
    

