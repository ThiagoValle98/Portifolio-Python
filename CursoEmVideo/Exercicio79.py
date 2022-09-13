menu = True
valores = []
while menu == True:
    escolha = str(input("Deseja adicionar algum valor a lista [S/N]?\n")).strip().upper()
    if escolha == "N":
        menu == False
        break
    else:
        valor = int(input("Digite o  valor para se adicionar:\n"))
        contador = valores.count(valor)
        if contador > 0 :
            print("Valor repetido, não foi cadastrado")
        else:
            valores.append(valor)
            print("Valor adicionado com sucesso")



print("Os valores digitados foram: {}".format(sorted(valores)))
