num1, num2 = input('Digite dois números inteiros : ').split(" ")
if int(num1) == int(num2):
    print("Os dois números tem o mesmo valor ")
elif int(num1) > int(num2):
    print("O número {} é maior que o número {}  ".format(num1,num2))
else:
    print("O número {} é maior que o número {}  ".format(num2,num1))
