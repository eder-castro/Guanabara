nome = input("Digite o seu mome completo: ")
print("Analisando seu nome...")
print("Seu nome em maiúsculas fica: {}".format(nome.upper()))
print("E este é seu nome em minúsculas: {}".format(nome.lower()))
'''n = 0
for letra in nome:
    if(letra != " "):
        n += 1
print(n)'''
print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(separa[0].capitalize(),len(separa[0])))