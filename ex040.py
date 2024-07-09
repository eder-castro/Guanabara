n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3)/3
if (media <5):
    print (f"Sua média foi {media:.2f} e você está REPROVADO!")
elif (media < 7):
    print (f" Sua média foi {media:.2f} e você está de RECUPERAÇÃO!")
else:
    print(f"PARABÉNS!!! Voce foi aprovado com média {media:.2f}!")