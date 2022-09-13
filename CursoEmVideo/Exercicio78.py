lista =[]
for n in range(0,5):
    lista.append(int(input("Digite valores para lista ")))
print("O maior valor desta lista é {} e ele está na {}ª posição".format(max(lista),(lista.index(max(lista))+1)))
print("O menor valor desta lista é {} e ele está na {}ª posição".format(min(lista),(lista.index(min(lista))+1)))