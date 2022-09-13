num = int(input('Digite um número? '))
fatorial = 1 
lista =[]
contador = num
while num > 1:
    fatorial *= num
    num -=1
    lista.insert(0,num)
print('{}! = {}'.format(contador, fatorial))

    

