n = int(input('Digite um valor para ser tabulado : '))
contador = 0
teste = True  
while teste == True :
    if n < 0:
        print("Programa encerrado")
        teste == False
        break 
    else: 
        print('{} * {} = {}'.format(n, contador, n*contador))
        contador+=1
        if contador > 10:
            n = int(input('Digite um valor para ser tabulado : '))
            contador = 0