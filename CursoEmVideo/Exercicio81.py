menu = True
valores = []
while menu == True:
    escolha = str(input("Deseja inserir algum valor? [S/N] \n")).strip().upper()
    if escolha == "N":
        menu = False
        print("Programa encerrado")
        break
    elif escolha != "N" and escolha != "S":
        print("Digito inválido")
        continue
    else:
        num = int(input("Digite o valor desejado: \n"))
        valores.append(num)


print("Sua lista de valores{}".format(valores))
print("Ela contem {} valores".format(len(valores)))
print(sorted(valores,reverse=True))
for n in valores:
    if n == 5:
        print("O numero 5 está na lista na posição {}".format(valores.index(n)+1))
