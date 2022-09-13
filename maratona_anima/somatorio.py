teste = int(input())
A=0
B=0 
somas = []
while A < teste:
    numeros = input().split(";")
    numeros_int = [int(n) for n in numeros]
    soma= sum(numeros_int)
    somas.insert(A,soma)
    A= A+1
for A in range(teste):
    if somas[A] != somas[-1]:
        print(somas[A])
    else:
        print(somas[A],end="")
        A=A+1
    