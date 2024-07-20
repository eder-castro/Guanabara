print ("=×" * 15)
print ("{: ^32}".format(" 10 TERMOS DE UMA P.A. " ))
print ("=×" * 15)
termo = int(input("Digite o primeiro termo: "))
fator = int(input("Digite o fator da progressão: "))
print (f"{termo} ", end = '')
num = termo
for i in range(1, 10):
    num += fator
    print (f" => {num}", end = '')
