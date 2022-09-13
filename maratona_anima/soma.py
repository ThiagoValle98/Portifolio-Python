teste = int(input())
A = 0
somas=[]
while A < teste :
    num1,num2 = input().split(" ")
    soma= int(num1) + int(num2)
    somas.insert(A,soma)
    A = A+1
for A in range(teste):
    if somas[A] != somas[-1]:
        print(somas[A])
    else:
        print(somas[A],end="")
    A = A+1






 
