from random import Random, random
import random
nomesalunos = input('Digite os nomes dos alunos ').split(" ")
nome = random.randint(0,3)
print('O aluno que irá apagar é {}'.format(nomesalunos[nome]))