P = int(input())
valornota100 = 100
valornota50 = 50 
valornota20 = 20
valornota10 = 10 
valornota5 = 5 
valornota2 =2 
valornota1=1
notas100 = P // valornota100
rest100 = P % valornota100
notas50 = rest100 // valornota50
rest50 = rest100 % valornota50
notas20 = rest50 // valornota20
rest20 = rest50 % valornota20
notas10 = rest20 // valornota10
rest10 = rest20 % valornota10
notas5 = rest10 // valornota5
rest5 = rest10 % valornota5
notas2 = rest5 // valornota2
rest2 = rest5 % valornota2
notas1 = rest2 // valornota1



print(notas100, "nota(s) de R$",valornota100)
print(notas50, "nota(s) de R$",valornota50)
print(notas20, "nota(s) de R$",valornota20)
print(notas10, "nota(s) de R$",valornota10)
print(notas5, "nota(s) de R$",valornota5)
print(notas2, "nota(s) de R$",valornota2)
print(notas1, "nota(s) de R$",valornota1,end="")