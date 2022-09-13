largura, altura = input('Qual a largura e altura da parede: ').split(" ")
area = int(largura)*int(altura)
litros = area/2
print('A área da parede é de {0} m2 \nVocê vai gastar {1} litros de tinta'.format(area,litros))