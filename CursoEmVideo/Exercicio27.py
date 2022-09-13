nome = str(input('Digite seu nome completo: ')).lower().strip().split(" ")
print('Seja bem Vindo {} {}'.format(nome[0].capitalize(),nome[-1].capitalize()))