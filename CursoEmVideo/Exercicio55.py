listapeso = []
for a in range (0,6):
    peso = float(input("Digite seu peso: "))
    listapeso.insert(a,peso)
print("O maior peso é de {} e o menor é de {} ".format(max(listapeso),min(listapeso)))