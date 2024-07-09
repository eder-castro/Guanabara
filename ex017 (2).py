'''from math import sqrt, pow
cat1 = float(input("Qual o comprimento do primeiro cateto?"))
cat2 = float(input("Qual o comprimento do segundo cateto?"))
hip = sqrt(pow(cat1,2) + pow(cat2,2))
print("O comprimento da Hipotenusa é {:.2f}".format(hip))'''
from math import hypot
cat1 = float(input("Digite o comprimento do primeiro cateto: "))
cat2 = float(input("Digite o comprimento do segundo cateto: "))
hip = hypot(cat1,cat2)
print("A Hipotenusa tem o comprimento de {:.2f}".format(hip))