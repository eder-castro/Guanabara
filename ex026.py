frase = str(input("Digite uma frase: ")).strip().upper()
primeiraposicao = frase.find('A')+1
vezes = frase.count('A')
ultimaposicao = frase.rfind('A')+1
print("A letra A aparece pela primeira vez na posição {}:".format(primeiraposicao))
print("A letra A aparece {} vezes".format(vezes))
print("A última letra A está na posição {}".format(ultimaposicao))