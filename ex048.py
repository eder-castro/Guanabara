itens = 0
soma = 0
for cont in range(1, 501, 2):
    if (cont % 3 == 0):
        itens += 1
        soma += cont
print (f"A soma dos {itens} números solicitados é {soma}")