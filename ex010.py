#conversor de moedas
usd = 4.90
eur = 5.20
lib = 4.70
peso = 0.75
cotacao = {'Dolar': usd, 'Euro': eur, 'Libra': lib, 'Peso': peso}
for chave in cotacao:
    print("{} - {}".format(chave, cotacao[chave]))
moeda = input("Escolha uma moeda: ")
vlr = float(input("Digite o valor em {} para a conversao em Reais: ".format(moeda.capitalize())))
print("{} {} valem {} Reais na minha cotacao!".format(vlr,moeda.capitalize(),(cotacao[moeda.capitalize()]*vlr)))