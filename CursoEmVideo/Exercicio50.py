lista = []
for a in range (0,6):
    numero = int(input("Digite os numeros para possibilidade de soma: "))
    if numero % 2 == 0:
        lista.insert(a,numero)
print("Os números pares são {} e a soma deles é {}".format(lista,sum(lista)))



        

