from random import randint
from time import sleep
maq = randint(0,2)
opc = ("PEDRA","PAPEL","TESOURA")
print ("{:=^40}".format(" VAMOS JOGAR JO KEN PO! "))
print ("( 0 ) PEDRA")
print ("( 1 ) PAPEL")
print ("( 2 ) TESOURA")
jogada = int(input("Qual a sua jogada? "))
print ("JO")
sleep (1)
print ("KEN")
sleep (1)
print ("PO")
print ("-=" * 20)
print(f"Eu escolhi {opc[maq]}!")
print (f"Você escolheu {opc[jogada]}!")
print ("-=" * 20)
if (maq == jogada):
    res = "EMPATAMOS"
elif (maq == 0 and jogada == 2 or maq == 1 and jogada == 0 or maq == 2 and jogada == 1):
    res = "EU GANHEI!!!"
else:
    res = "VOCÊ GANHOU!!!"
print (res)