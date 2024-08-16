print ("=×" * 15)
print ("{: ^32}".format(" TERMOS DE UMA P.A. " ))
print ("=×" * 15)
termo = int(input("Digite o primeiro termo: "))
fator = int(input("Digite o fator da progressão: "))
print (f"{termo} => ", end = '')
num = termo
qtd = 10
cont = 1
soma = 10
while (qtd != 0) :
    while (cont < qtd):
        num += fator
        print (f"{num} => ", end = '')
        cont += 1
    print("PAUSA")
    qtd = int(input("Quantos termos mais? "))
    soma += qtd
print(f"Progressao finalizada com {soma} termos!")