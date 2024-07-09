print("Verificarei se as 3 retas que você informar formam um triângulo...")
r1 = float(input("Informe o comprimento da primeira reta: "))
r2 = float(input("Agora o comprimento da segunda reta: "))
r3 = float(input("E finalmente, informe o comprimento da última reta: "))
if (((r1 + r2) > r3) and ((r2 + r3) > r1) and ((r1 + r3) > r2)):
    if(r1 == r2 and r2 == r3):
        print("As retas formam um triangulo equilatero!")
    elif (r1 == r2 or r1 == r3 or r2 == r3):
        print("As retas informadas formam um triangulo Isosceles!")
    else:
        print("As 3 retas informadas formam um triângulo escaleno!")
else:
    print("As retas informadas nāo formam um triângulo!")



'''
a + b > c
b + c > a
a + c > b
'''
'''
isosceles - 2 lados mesma medida
equilatero - iguais
escaleno - diferentes
'''    
