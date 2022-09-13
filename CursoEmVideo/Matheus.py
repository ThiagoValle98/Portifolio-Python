import random
escolha = random.randint(1,2)
pergunta = str(input("Faça uma pergunta?  Que te direi a resposta\n" ))
if escolha == 1:
    print("Sim",escolha)
else:
    print("Não",escolha)