frase = str(input("Digite uma frase! ")).strip().upper()
separa = frase.split()
junta = ''.join(separa)
invert = junta[::-1]
print (invert)
if (junta == invert):
    print ("A frase digitada é um PALINDROMO")
else:
    print ("A frase escolhida NÃO É um PALINDROMO")
'''
frase_inv = [] #cria lista vazia
frase_div = [] #cria lista vazia
for n in range(len(frase), 0, -1):
    frase_inv.append(frase[n-1])
for n in range (0, len(frase)):
    frase_div.append(frase[n])
print (frase_inv)
print (frase_div)
print (frase_div == frase_inv)
'''
