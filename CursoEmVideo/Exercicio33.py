num1,num2,num3 = input("Digite três numeros: ").split(" ")
lista = [num1,num2,num3]
maior = max(lista)
menor = min(lista)
print('O maior número é {} e o menor número é {}'.format(maior,menor))