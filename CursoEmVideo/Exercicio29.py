velocidade = int(input("Digite a velocidade do carro?\n"))
if velocidade > 80 :
    multa = velocidade - 80 
    valor = 7.00*multa
    print("Você foi multado {}R$ a pagar !".format(valor))