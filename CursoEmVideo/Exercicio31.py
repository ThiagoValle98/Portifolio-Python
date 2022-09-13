km = int(input("Quantos Kilometros deseja Viajar: "))
if km<=200:
    print('Sua viagem custará {}R$'.format(km*0.5))
else:
    print('Sua viagem custará {}R$'.format(km*0.45))
