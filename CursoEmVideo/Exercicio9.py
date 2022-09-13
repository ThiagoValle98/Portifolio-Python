numero = int(input('Digite um numero '))
A=0
print('Taboada do {}'.format(numero))
while A <= 100:
    resultado = numero * A
    print('{0} * {1} = {2}'.format(numero,A,resultado))
    A=A+1
