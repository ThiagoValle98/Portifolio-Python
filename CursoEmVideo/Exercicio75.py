num = (int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")))
print(num)
print("o numero 9 apareceu {} vezes".format(num.count(9)))
if 3 in num:
    print("O primeiro valor tres aparece na posição {} ".format(num.index(3)+1))
else:
    print("O 3 Não aparece em nenhuma posição")
for n in num :
    if n % 2== 0:
        print(n, end=" ")
