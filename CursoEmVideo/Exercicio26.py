frase = str(input('Digite uma frase ')).lower().strip()
a = frase.count("a")
posi = frase.find("a")
print('A letra A aparece {} vezes\nO A aparece pela primeira vez na posiçao {}\nA sua ultima possição é {}'.format(a,posi+1,frase.rfind("a")+1))