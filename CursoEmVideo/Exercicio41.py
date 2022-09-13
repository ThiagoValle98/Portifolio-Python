import datetime
ano_hoje = datetime.date.today().year
ano_nasc = int(input('Coloque seu ano de nascimento: '))
difernça = ano_hoje - ano_nasc
if difernça < 7 :
    print("Você não compete ")
elif difernça <= 10 :
    print(" Você é mirim ")
elif difernça <= 12 :
    print(" Você é petiz ")
elif difernça <= 14 :
    print(" Você é infantil ")
elif difernça <= 16 :
    print(" Você é juvenil ")
elif difernça <= 19 :
    print(" Você é júnior ")
elif difernça > 19 :
    print(" Você é Sênior ")
