contador = 0
soma = 0 
n = int(input('Digite um número: \n'))
while n != 999:
    if n == 999:
        break
    else:
        soma += n
        contador +=1
        n =int(input('Digite um número: \n'))
print("Você digitou {} números e a soma deles foi de {} ".format(contador,soma))
    