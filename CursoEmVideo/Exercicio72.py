tupla = ("ZERO","UM","DOIS","TRÊS","QUATRO","CINCO","SEIS","SETE","OITO","NOVE","DEZ","ONZE","DOZE","TREZE","QUATORZE","QUINZE","DEZESSEIS","DEZESSETE","DEZOITO","DEZENOVE","VINTE")
num = int(input("Digite um número de 0 a 20:\n"))
while num < 0 :
    num = int(input("Numero Invalido!!! Digite um número de 0 a 20:\n"))
while num > 20 :
    num = int(input("Numero Invalido!!! Digite um número de 0 a 20:\n"))
print("Você digitou o numero {}".format(tupla[num]))