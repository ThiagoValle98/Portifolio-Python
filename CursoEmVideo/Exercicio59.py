valor1 = int(input('Digite o primeiro valor?\n'))
valor2 = int(input('Digite o segundo valor?\n'))
menu = int(input('Digite (1) para somar\nDigite (2) para multiplicar\nDigite (3) para o maior\nDigite (4) para novos numeros\nDigite (5) para sair\n'))
while menu < 5 and menu > 0 :
    if menu == 1:
        soma = valor1 + valor2
        print('{} + {} = {}'.format(valor1,valor2,soma))
        menu = int(input('Digite (1) para somar\nDigite (2) para multiplicar\nDigite (3) para o maior\nDigite (4) para novos numeros\nDigite (5) para sair\n'))
    elif menu == 2:
        multi = valor1*valor2
        print('{} * {} = {}'.format(valor1,valor2,multi))
        menu = int(input('Digite (1) para somar\nDigite (2) para multiplicar\nDigite (3) para o maior\nDigite (4) para novos numeros\nDigite (5) para sair\n'))
    elif menu == 3:
        maior = max(valor1,valor2)
        menor = min(valor1,valor2)
        print('{} > {} '.format(maior,menor))
        menu = int(input('Digite (1) para somar\nDigite (2) para multiplicar\nDigite (3) para o maior\nDigite (4) para novos numeros\nDigite (5) para sair\n'))
    elif menu == 4:
        valor1 = int(input('Digite o primeiro valor?\n'))
        valor2 = int(input('Digite o segundo valor?\n'))
        menu = int(input('Digite (1) para somar\nDigite (2) para multiplicar\nDigite (3) para o maior\nDigite (4) para novos numeros\nDigite (5) para sair\n'))

