numero1,numero2 = input().split(" ")
if int(numero1) > 0 and int(numero2) > 0:
    print("R1",end="")
if int(numero1) < 0 and int(numero2) < 0:
    print("R3",end="")
if int(numero1) > 0 and int(numero2) < 0:
    print("R4",end="")
if int(numero1) < 0 and int(numero2) > 0:
    print("R2",end="")
if int(numero1) == 0 and int(numero2) == 0:
    print("NO ALVO!",end="")


