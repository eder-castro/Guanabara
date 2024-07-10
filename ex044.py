print("{:=^32}".format(" LOJINHA DO EDER "))
valor = float(input("Qual o valor da compra? R$ "))
print("\n {:=^31}".format(" FORMAS DE PAGAMENTO "))
print('''Digite a opcao desejada:
( 1 ) Á vista - Dinheiro ou PIX
( 2 ) Á vista - Débito
( 3 ) Até 2 x - Crédito
( 4 ) 3 x ou mais - Crédito\n''')
forma = int(input("Escolha uma forma de pagamento: "))
if (forma == 1):
    vlr_pg = valor - valor * 10/100
elif (forma == 2):
    vlr_pg = valor - valor * 5/100
elif (forma == 3 or forma == 4):
    qt_parc = int(input("Em quantas vezes? "))
    if (forma == 3):
        vlr_pg = valor
        if (qt_parc > 2):
            print (f"Você digitou um número incorreto ({qt_parc}) de parcelas")
            exit
    else:
        vlr_pg = valor + valor * 10/100
if (forma == 1 or forma == 2):
    print (f"O valor final de sua compra de R$ {valor:.2f} será de R$ {vlr_pg:.2f}")
elif (forma == 3 or forma == 4):
    print (f"O valor final de sua compra de R$ {valor:.2f} será de R$ {vlr_pg:.2f} dividido em {qt_parc} parcelas de R${vlr_pg / qt_parc:.2f}")
else:
    print("Forma de pagamento incorreta!")
