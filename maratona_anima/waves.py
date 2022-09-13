for i in range(int(input())):
    numeros = input().split()
    if (int(numeros[0])) + (int(numeros[1])) <= int(numeros[2]):
        if i == 0: print("CABE!", end='')
        else: print("\nCABE!", end='')
    else:
        if i == 0: print("NAO CABE!", end='')
        else: print("\nNAO CABE!", end='')