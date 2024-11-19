num = cont = media = soma = maior = menor = 0
res = "S"
while res != "N":
    num = int(input("Digite um número: "))
    res = str.upper(input("Deseja continuar? [S/N]"))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f"Você digitou {cont} números e a média deles é {media}!")
print(f"O maior valor foi {maior} e o menor valor foi {menor}!")