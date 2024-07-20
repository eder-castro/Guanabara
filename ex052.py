num = int(input("Digite um número: "))
cont = 0
n = num
for n in range(num, 0, -1):
    if (num % n == 0):
        cont += 1
if (cont == 2):
    print (f"O número {num} É um número Primo!")
else:
    print (f"O número {num} NÃO é um número Primo!")