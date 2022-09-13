teste = int(input())
A=0 
resposta=[]
while A<teste :
    ovni1, ovni2, plataforma = input().split(" ")
    resultado = int(ovni1) + int(ovni2)
    qtde = len(resposta)
    if resultado <= int(plataforma):
        if A == 0:
            print("CABE!", end='')
        else:
            print("\nCABE!",end='')
    else:
        if A==0:
            print("NAO CABE!",end='')
        else:
            print("\nNAO CABE!",end='')
    A=A+1



    


