import random
menu = input('Bem vindo ao advinhador deseja jogar? SIM para continuar, Não para Sair\n').upper().strip()
tentativas = 0
while menu == "SIM":
    numero = random.randint(0,10)
    escolha = int(input('Qual número de 0 a 10 eu pensei? '))
    tentativas +=1
    if escolha == numero:
        print("Você acertou em {} tentativas".format(tentativas))
        menu= "Não"
    else: 
        print("Voce escolheu {}, e o numero correto era {}".format(escolha,numero))
    

    
    