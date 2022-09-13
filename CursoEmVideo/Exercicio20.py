import random 


nome1 = input('Digite o nome dos alunos: ')
nome2 = input('Digite o nome dos alunos: ')
nome3 = input('Digite o nome dos alunos: ')
nome4 = input('Digite o nome dos alunos: ')
nome=[nome1,nome2,nome3,nome4]
random.shuffle(nome)
print('A ordem da apresentação é : {} '.format(nome))

