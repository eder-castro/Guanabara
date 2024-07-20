from datetime import date
nasc = []
menor = 0
maior = 0
for p in range (0, 7):
    ano = int(input("Digite o ano de nascimento: "))
    nasc.append([ano])
    if (ano >= 2006):
        menor += 1
    else:
        maior += 1
print (f"Nesta lista temos {maior} pessoas maiores de 18 anos e {menor} pessoas menores.")
    