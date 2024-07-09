#digite algo...
#espaco = True
ent = input("Digite algo: ")
#qual o tipo primitivo?
print("O dado digitado é do tipo {}".format(type(ent)))
#é so espacos?
espaco = ent.isspace()
print("O dado digitado é somente espaço? {}".format(espaco))
#e num?
numerico = ent.isnumeric()
print("O dado digitado é numerico? {}".format(numerico))
#e alfabetico?
alfabetico = ent.isalpha()
print("O dado digitado é alfabetico? {}".format(alfabetico))
#e alfanum?
alfanum = ent.isalnum()
print("O dado digitado é alfanumerico? {}".format(alfanum))
#esta em maiusc?
maius = ent.isupper()
print("O dado digitado é letra maiuscula? {}".format(maius))
#esta em minusc?
minus = ent.islower()
print("O dado digitado é letra minuscula? {}".format(minus))
#esta capitalizado?
capital = ent.istitle()
print("O dado digitado é Capitalizado? {}".format(capital))