menu = True
valores=[]
while menu == True:
    escolha = str(input("Deseja salvar um valor? [S/N]\n")).strip().upper()
    if escolha == "N":
        menu = False
        print("Programa Encerrado")
        break
    elif escolha != "N" and escolha != "S":
        print("Dígito inválido")
        continue
    else:
        num = int(input("Digite o valor a ser salvo:\n"))
        valores.append(num)

valorespares = []
valoresimpares = []
for n in valores:
    if n % 2 == 0:
        valorespares.append(n)
    elif n % 2 == 1:
        valoresimpares.append(n)


print("Todos os valores são {}".format(valores))
print("Todos os valores pares são {}".format(valorespares))
print("Todos os valores impares são {}".format(valoresimpares))
        

