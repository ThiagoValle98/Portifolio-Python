import datetime
listamaiores = []
listamenores = []
for a in range (0,7):
    anonasc=int(input("Qual seu ano de nascimento "))
    anohoje = datetime.date.today().year
    idade = anohoje - anonasc
    if idade >= 18:
        listamaiores.insert(a,idade)
    else:
        listamenores.insert(a,idade)
print("{} pessoas são maiores de idade e {} pessoas são menores de idade ".format(len(listamaiores),len(listamenores)))

