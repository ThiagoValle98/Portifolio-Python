contador = 0
soma = 0
num = int(input('Digite um numero ? \n'))
while num != 999:
    contador +=1
    soma =+ num 
    num = int(input('Digite um numero ? \n'))
print("Foram digitados {} e sua soma foi de {}".format(contador,soma))