from random import randint
print ("-" * 36)
print("Jogo do PAR ou ÍMPAR")
print ("-" * 36)
aleat = randint(0, 100) #número de escolha do computador
winner = ""
ganhas = 0
while winner != "PERDEU!":
    n = int(input("Escolha um número: ")) #número de escolha do usuário
    escolha = str.upper(input("Você escolhe PAR ou ÍMPAR? ")) #opção do usuário
    soma = n + aleat #soma dos 2 números
    #resultado
    if soma % 2 == 0:
        res = "PAR"
    else:
        res = "ÍMPAR"

    print ("-" * 36)
    print(f"Seu número foi {n} e o meu número foi {aleat}, totalizando {soma}, portanto {res}!")
    print ("-" * 36)

    if escolha == "PAR" or escolha == "P":
        escolha = "PAR"

    if escolha == "IMPAR" or escolha == "I" or escolha == "ÍMPAR":
        escolha = "ÍMPAR"

    if escolha == res:
        winner = "GANHOU! PARABÉNS!"
        ganhas += 1
    else:
        winner = "PERDEU!"
print(f"Você escolheu {escolha} e VOCÊ {winner}!")
