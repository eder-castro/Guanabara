from random import randint
from time import sleep
num = randint(0,5)
print("-=-" * 20)
print("Estou pensndo em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
tentativa = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if(tentativa == num):
    print("PERDI!!! Você Acertou!!!")
else:
    print("GANHEI!!! Você Errou!!!")
    print("Meu número era {}".format(num))
