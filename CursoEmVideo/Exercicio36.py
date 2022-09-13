valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o valor do seu salário mensal : '))
anos = int(input('Quantos anos pretende pagar: '))
porcentagem = valor_salario * 0.30
prestaçao = valor_casa / (anos * 12)
if porcentagem >= prestaçao:
    print('Empréstimo aprovado você pagará R${} de prestações mansais'.format(prestaçao))
else:
    print('Empréstimo negado sem renda suficiente ')
