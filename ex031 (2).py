dist = float(input("Qual a distância da sua viagem? "))
if dist <= 200:
    print("O valor da passagem para esta viagem é de R$ {}".format(dist * 0.50))
else:
        print("A passagem para esta viagem custará R$ {}".format(dist * 0.45))
        