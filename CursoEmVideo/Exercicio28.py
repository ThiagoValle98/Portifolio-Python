import random
numero = random.randint(0,5)
menu = input('Bem vindo ao advinhador deseja jogar? SIM para continuar, Não para Sair\n').upper().strip()
while menu == "SIM":
    escolha = int(input('Qual número de 0 a 5 eu pensei? '))
    if escolha == numero:
        print("Parabens Voce acertou!!!")
        menu = input("Deseja continuar?\n").upper().strip()
    else:
        print("Tente Novamente")
        menu = input("Deseja continuar?\n").upper().strip()
    