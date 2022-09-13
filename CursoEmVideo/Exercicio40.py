nota1, nota2 = str(input('Digite suas notas :')).strip().split(" ")
media = (int(nota1)+ int(nota2))/2
if media < 5 :
    print("Se fudeu repete ")
elif media > 5 and media < 6.9:
    print("Vai ter que ficar as férias estudando otário ")
elif media > 6.9 and media < 10 :
    print("Não fez mais que a obrigação ")
else:
    print("Párabens você é foda ")