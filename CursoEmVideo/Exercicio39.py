from datetime import date
sexo = input('Digite seu sexo: [M] para masculino, e [F] para feminino: ').strip().upper()
ano = int(input('Digite seu ano de nascimento: '))
ano_hoje = date.today().year
if sexo == "F" :
    print("Pessoas do sexo feminino não precisam alistar ")
elif sexo == "M" and ano_hoje - ano == 18 :
    print("Está na hora de alistar vá agora ao exército mais próximo ")
elif sexo == "M" and ano_hoje - ano < 18 :
    diferença = ((ano_hoje - ano) - 18)*-1
    print("Você ainda irá se alistar em {} anos ".format(diferença))
elif sexo == "M" and ano_hoje - ano > 18 :
    diferença2 = (ano_hoje - ano) - 18
    print("Você já deveria ter se alistado em {} anos, Procure já o exército mais próximo e se regularize ".format(diferença2))