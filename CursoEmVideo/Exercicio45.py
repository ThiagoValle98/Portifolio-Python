import random
jokenpo = ["Pedra","Papel","Tesoura"]
escolha_pc = random.choice(jokenpo)
escolha_jogador = str(input('Bem Vindo ao Jokenpô escolha sua jogada, Pedra, Papel ou Tesoura: ')).strip().capitalize()
if escolha_pc == "Pedra" and escolha_jogador == "Pedra":
    print('EMPATE')
elif escolha_pc == "Pedra" and escolha_jogador == "Tesoura":
    print("Derrota")
elif escolha_pc == "Pedra" and escolha_jogador == "Papel":
    print("Vitória")
elif escolha_pc == "Tesoura" and escolha_jogador == "Pedra":
    print("Vitória")
elif escolha_pc == "Tesoura" and escolha_jogador == "Tesoura":
    print("EMPATE")
elif escolha_pc == "Tesoura" and escolha_jogador == "Papel":
    print("Derrota")
elif escolha_pc == "Papel" and escolha_jogador == "Pedra":
    print("Derrota")
elif escolha_pc == "Papel" and escolha_jogador == "Tesoura":
    print("Vitória")
elif escolha_pc == "Papel" and escolha_jogador == "Papel":
    print("EMPATE")