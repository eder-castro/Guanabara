from datetime import date
nasc = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - nasc
if (idade <= 5):
   print("Olá, você é um bebê! Deveria estar assistindo galinha pintadinha!!!")
elif (idade < 18):
    print (f"Voce irá se alistar daqui a {18 - idade} anos")
elif (idade == 18):
    print ("PROCURE A JUNTA DE ALISTAMENTO MILITAR MAIS PRÓXIMA COM URGÊNCIA!!! VOCÊ DEVE SE ALISTAR ESTE ANO!")
else:
    print (f"Seu alistamento deveria ter sido feito há {idade - 18} anos!")
