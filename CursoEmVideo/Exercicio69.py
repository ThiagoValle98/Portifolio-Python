qtde_idade = 0
menu = True
qtde_homens = 0
qtde_mulheres=0
while menu == True:
    print("Novo Cadastro SUS:\n")
    idade = int(input("Digite sua idade: \n"))
    if idade >= 18:
        qtde_idade+=1
    sexo = str(input("Digite seu sexo? [M/F]\n")).upper().strip()
    if sexo == "M":
        qtde_homens+=1
    elif sexo == "F" and idade <= 20:
        qtde_mulheres+=1
    menu1 = str(input("Deseja Cadasrar mais uma pessoa? [S/N]\n")).upper().strip()
    if menu1 == "S":
        menu = True 
    elif menu1 == "N":
        menu = False
        break
print("São {} maiores de idade, foram {} homens, e {} mulheres tem menos de 20 ".format(qtde_idade,qtde_homens,qtde_mulheres))