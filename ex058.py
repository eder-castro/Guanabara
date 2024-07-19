from random import randint
from time import sleep
num = randint(0,10)
print("-=-" * 20)
print("Sou seu computador...")
print(f"Estou pensando em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)
tentativa = int(input("Em que número eu pensei? "))
palpites = 1
while(tentativa != num):
    print("PROCESSANDO...")
    sleep(1)
    palpites += 1
    if(num > tentativa):
        print("O número é maior!")
    else:
        print("O número é menor!")
    tentativa = int(input("GANHEI!!! Você ERROU! Tente novamente: "))
print(f"PERDI!!! Parabéns!!! Você Acertou em {palpites} tentativas!!!")
print("O número era {}".format(num))
