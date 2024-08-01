print ("=×" * 15)
print ("{: ^32}".format(" 10 TERMOS DE UMA P.A. " ))
print ("=×" * 15)
termo = int(input("Digite o primeiro termo: "))
fator = int(input("Digite o fator da progressão: "))
print (f"{termo} ", end = '')
num = termo
cont = 1
while (cont < 10):
    num += fator
    cont += 1
    print (f" => {num}", end = '')