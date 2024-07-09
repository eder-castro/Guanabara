'''18,5 - abaixo do peso
25 - peso ideal
30 - sobrepeso
40 - obeso
acima - obesidade morbida
'''
'''
IMC = peso / (altura x altura)
'''
peso = float(input("Qual o seu peso? "))
alt = float(input("Qual a sua altura? "))
imc = peso / pow(alt,2)
if(imc <= 18.5):
    classif = "Abaixo do peso!"
elif (imc <= 25):
    classif = "No peso ideal!"
elif (imc <= 30):
    classif = "Com sobrepeso!"
elif (imc <= 40):
    classif = "Obeso! Cuidado"
else:
    classif = "Obeso mórbido! Procure um médico!"
print(f"Seu peso é: {peso}")
print(f"E sua altura é: {alt}")
print(f"Seu IMC calculado é: {imc:.2f}")
print(f"Pela tabela do ministerio da saúde, voce está {classif}")