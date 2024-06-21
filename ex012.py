preco = float(input("Digite o preço: "))
desc = (float(input("Digite a porcentagem de desconto: "))/100)
novo_preco = preco - (desc * preco)
print("O produto que custava {} na promoção com {} % de desconto, vai custar {}".format(preco,desc*100,novo_preco))