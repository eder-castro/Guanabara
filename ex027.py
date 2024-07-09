nome = str(input("Digite seu nome completo: ")).strip().upper()
lista_nome = nome.split()
prim_nome = lista_nome[0]
ult_nome = lista_nome[len(lista_nome)-1]
print("Muito prazer em te conhecer")
print("Seu primeiro nome é {}".format(prim_nome))
print("Seu último nome é {}".format(ult_nome))