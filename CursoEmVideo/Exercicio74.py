from random import randint
tupla = ("")
for n in range (0,5):
    num = randint(1,10)
    num = str(num)
    tuplanum=(num)
    tupla = tupla + tuplanum
print("Os numeros gerados foram {} {} {} {} {} ".format(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4]))
print("O maior valor é {}".format(max(tupla)))
print("o menor valor é {}".format(min(tupla)))





