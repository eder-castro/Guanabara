soma = 0
cont = 0
for n in range(1,7):
    num = int(input(f"Digite o {n}° número: "))
    if (num % 2 == 0):
        soma += num
        cont += 1
print(f"A soma dos {cont} números pares desta sequência é {soma}!!!")
