from time import sleep
print("-=-"*10)
print("Cálculo de parcela e aprovaçāo de financiamento")
print("-=-"*10)
vlr = float(input("\nDigite o valor a financiar: "))
sal = float(input("informe o seu salario: "))
qt_parc = int(input("Em quantos meses deseja financiar este valor? "))
print(f"O valor solicitado para financiamento foi de R$ {vlr:_.2f}".replace('.',',').replace('_','.'))
print(f"O salário informado foi R$ {sal:_.2f}".replace('.',',').replace('_','.'))
print(f"Você escolheu financiar em {qt_parc:d} meses")
print("ANALISANDO...")
sleep(3)
perc = (vlr / qt_parc) / sal
print(f"{perc:.2%}")
if((vlr / qt_parc) <= (sal * 0.3)):
    print("Parabéns, seu financiamento foi aprovado!")
else:
    print("REPROVADO!")
print(f"Para este financiamento, o valor da parcela seria R$ {vlr / qt_parc:.2f} ({perc:.2%} do seu salario)")

