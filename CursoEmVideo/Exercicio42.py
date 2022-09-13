reta1, reta2, reta3 = input('Digite os valores das retas : ').split(" ")
re_1 = int(reta1)
re_2 = int(reta2)
re_3 = int(reta3)
lista = [re_1,re_2,re_3]
maior = max(lista)
somalista = sum(lista) - (2*maior)
if somalista > 0:
    print('Pode ser um triângulo ')
    if re_1 == re_2 and re_2== re_3:
        print("Triângulo Equilatero ")
    elif re_1 == re_2 or re_1 == re_3 or re_2 == re_3:
        print("Triângulo Isóseles ")
    elif re_1 != re_2 and re_1 != re_3 and re_2 != re_3:
        print("Triangulo Escaleno ")
else:
    print('Não pode ser um triângulo')