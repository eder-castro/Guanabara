#60/dia
#0,15/km
km = float(input("Digite a quilometragem rodada: "))
dias = int(input("Digite a quantidade de dias de aluguel: "))
valor = 60 * dias + 0.15 * km
print("O valor a pagar é de R$ {}".format(valor))