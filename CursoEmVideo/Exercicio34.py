salario = int(input('Qual o valor do seu salario ?\n'))
if salario >= 1250:
    print("Seu novo salário é de {} R$".format(salario*1.10))
else:
    print('Seu novo salário é de {} R$'.format(salario*1.15))