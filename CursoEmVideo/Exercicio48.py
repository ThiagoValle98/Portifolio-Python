print("Soma dos multiplos de 3: ")
s = []
for a in range (1,501,2):
    if a % 3 == 0 :
        s.insert(0,a)
soma = sum(s)
print(soma)
    
