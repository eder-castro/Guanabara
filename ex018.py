from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print("Para o ângulo de {:.2f}º, o seno é {:.2f}".format(ang,seno))
print("Para o ângulo de {:.2f}º, o cosseno é {:.2f}".format(ang,cosseno))
print("Para o ângulo de {:.2f}º, a tangente é {:.2f}".format(ang,tangente))

