nomes = []
idades =[]
sexos =[]
media = (sum(idades)) / len(idades)
maioridadehomem = 0
nomemaisvelho = ""
for a in range (0,5):
    nome = str(input("Me informe seu nome : "))
    idade = int(input("Informe sua idade "))
    sexo = str(input("Informe seu sexo "))
    nomes.insert(a,nome)
    idades.insert(a,idade)
    sexos.insert(a,sexo)

