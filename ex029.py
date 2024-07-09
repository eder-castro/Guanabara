velocidade = int(input("Digite a velocidade do carro: "))
if(velocidade > 80):
    multa = (velocidade-80)*7
    print("MULTADO!!! Você ultrapassou o limite de velocidade que é 80km/h!")
    print("Você pagará R$ {:.2f} de multa por esta infração.".format(multa))
#else:
print("Boa viagem! Dirija com segurança!")
print("Tenha um ótimo dia!")