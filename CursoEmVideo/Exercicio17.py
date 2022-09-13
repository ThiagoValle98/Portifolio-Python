
import math
cateto_a = int(input('Digite valor do cateto: '))
cateto_o = int(input('Digite o valor do cateto '))
hipotenusa = cateto_a**2 + cateto_o**2
hipo = math.sqrt(hipotenusa)
print('Valor da hipotenusa é de {}'.format(hipo))
