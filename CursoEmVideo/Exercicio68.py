from random import randint
print("Vamos jogar par ou impár! ")
teste = True 
soma = 0
contador = 0
while teste == True:
    jogada = int(input('Digite um valor :\n'))
    escolha = str(input('Par ou ímpar? [P/I]:\n')).strip().upper()
    jogada_pc = randint(0,10)
    soma = jogada + jogada_pc
    print("Você jogou {} e o computador {}. O totatal deu {}.".format(jogada,jogada_pc,soma))
    if escolha == "P" and soma % 2 == 0:
        print('Você Venceu!\nVamos jogar novamente... ')
        contador+=1
    elif escolha == "I" and soma % 2 != 0:
        print('Você Venceu!\nVamos jogar novamente... ')
        contador+=1
    else:
        print("Você perdeu!\nGame Over, você venceu {} vezes.".format(contador))
        break