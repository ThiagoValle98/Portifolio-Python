ano = int(input("Digite o ano: "))
bi = ano%4
if bi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Este ano é bisexto ")
else:
    print("Este ano não é bissexto")