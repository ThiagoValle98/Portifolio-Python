soma = 0
contador = 0
menu = str(input('Deseja Digitar um numero? \n')).strip().upper()
while menu == "SIM":
    num = int(input('Digite um numero: \n'))
    soma += num
    contador +=1
    menu = input("Deseja continuar ?\n").strip().upper()
print("A média foi de {}".format(soma/contador))
