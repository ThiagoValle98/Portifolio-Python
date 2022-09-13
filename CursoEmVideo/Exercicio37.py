numero = int(input('Digite um número para conversação: '))
escolha = int(input('Digite [1] para conversão binária, [2] para conversão octal, [3] para conversão hexadecimal '))
if escolha == 1:
    binario = bin(numero)
    print('{} === {}'.format(numero,binario[2:]))
elif escolha == 2:
    octal = oct(numero)
    print('{} === {}'.format(numero,octal[2:]))
elif escolha == 3:
    hexa = hex(numero)
    print('{} === {}'.format(numero,hexa[2:]))
else:
    print("Digito incorreto programa encerrado!!!")