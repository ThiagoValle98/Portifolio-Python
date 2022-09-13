frase = str(input("Digite uma frase e veja se é um palíndromo ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
comprimento = len(junto)
for letra in range(comprimento -1 ,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print("TEMOS UM PALINDROMO")
else:
    print("NÂO TEMOS UM PALINDROMO")
    
