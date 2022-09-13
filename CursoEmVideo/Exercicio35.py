reta1, reta2, reta3 = input('Digite os valores das retas : ').split(" ")
re_1 = int(reta1)
re_2 = int(reta2)
re_3 = int(reta3)
lista = [re_1,re_2,re_3]
maior = max(lista)
somalista = sum(lista) - (2*maior)
if somalista > 0:
    print('Pode ser um triângulo ')
else:
    print('Não pode ser um triângulo')