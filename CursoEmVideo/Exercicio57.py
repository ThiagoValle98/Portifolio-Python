sexo = str(input('Digite seu sexo [M] para masculino ou [F] para feminino \n')).strip().upper()
if sexo == "M":
        print("Você é um homem ")
elif sexo =="F":
        print("Você é uma mulher ")
while sexo != "M" and sexo != "F":
    sexo=str(input('Dígito inválido digite novamente ')).strip().upper()



