num = int(input("Digite um número para calcular o seu fatorial: "))
fat = 1
cont = num
print(f"Calculando {num}! = ", end = '')
'''for i in range (num, 1, -1):
    fat = fat * i
    print (f"{i} x ", end = '')'''
while (cont > 1):
    fat = fat * cont
    print (f"{cont} x ", end = '')
    cont -= 1
print (f"{cont} = {fat}")