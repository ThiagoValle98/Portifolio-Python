num = int(input("Digite um número e verifique se ele é primo: "))
cont = 2
while cont < num:
    primo = num % cont
    if primo == 0 :
        print("ESTE NÚMERO NÃO É PRIMO ")
        break
    if primo != 0 and num == cont + 1:
        print("ESTE NÚMERO É PRIMO ")
    cont = cont+1

