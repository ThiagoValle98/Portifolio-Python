num1 = int(input())
s1 = input()
num2 = int(input())
s2 = input()
num3 = int(input())
if s1 == "+" and s2 == "+":
    result1= num1 + num2 + num3
    print(result1,end="")
if s1 == "+" and s2 == "-":
    result2= num1 + num2 - num3
    print(result2,end="")
if s1 == "+" and s2 == "*":
    result3= num1 + num2 * num3
    print(result3,end="")
if s1 == "+" and s2 == "/":
    if num3 == 0:
        print("erro",end="")
    else:
        result4 = num1+ num2 // num3
        print(result4,end="")
if s1 == "-" and s2 == "-":
    result5= num1 - num2 - num3
    print(result5,end="")
if s1 == "-" and s2 == "+":
    result6= num1 - num2 + num3
    print(result6,end="")
if s1 == "-" and s2 == "*":
    result7= num1 - num2 * num3
    print(result7,end="")  
if s1 == "-" and s2 == "/":
    if num3 == 0:
        print("erro",end="")
    else:
        result8 = num1- num2 // num3
        print(result8,end="")
if s1 == "*" and s2 == "+":
    result9= num1 * num2 + num3
    print(result9,end="")
if s1 == "*" and s2 == "-":
    result10= num1 * num2 - num3
    print(result10,end="")
if s1 == "*" and s2 == "*":
    result11= num1 * num2 * num3
    print(result11,end="")
if s1 == "*" and s2 == "/":
    if num3 == 0:
        print("erro",end="")
    else:
        result12 = num1* num2 // num3
        print(result12,end="")
if s1 == "/" and s2 == "+":
    if num2 == 0:
        print("erro",end="")
    else:
        result13 = num1 //num2 +num3 
        print(result13,end="")
if s1 == "/" and s2 == "-":
    if num2 == 0:
        print("erro",end="")
    else:
        result14 = num1 //num2 -num3 
        print(result14,end="")
if s1 == "/" and s2 == "*":
    if num2 == 0:
        print("erro",end="")
    else:
        result15 = num1 //num2 *num3 
        print(result15,end="")
if s1 == "/" and s2 == "/":
    if num2 == 0 and num3 ==0:
        print("erro",end="")
    else:
        result16 = num1 //num2 //num3 
        print(result16,end="")
