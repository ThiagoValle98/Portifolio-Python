termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a progressão: "))
pa = termo1*razao
while termo1 <= pa:
    print(termo1)
    termo1 = termo1 + razao 
    if termo1 > pa:
        razao=int(input('Deseja adicionar mais termos? '))
        while termo1 <= termo1 * razao:
                print(termo1)
                termo1 = termo1 + razao


    