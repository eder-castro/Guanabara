from datetime import date
ano = int(input("Digite um ano para verificar se ele é bissexto: (Para analisar o ano atual, digite 0) "))
if (ano == 0):
    ano = date.today().year
tst1 = ano%100
if (tst1 == 0):
    tst2 = ano%400
    if (tst2 == 0):
        print("{} é um ano bissexto".format(ano))
    else:
        print ("{} nāo é um ano bissexto".format(ano))
else:
    tst1= tst1%4
    if (tst1 == 0):
        print("{} é um ano bissexto".format(ano))
    else:
        print ("{} nāo é um ano bissexto".format(ano))
