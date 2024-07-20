soma_idade = 0
menor20 = 0
idade_max_masc = 0
nome_old_masc = ""
for p in range (1,5):
    nome = str(input(f"Digite o nome da {p} ° pessoa: "))
    idade = int(input(f"Digite a idade da {p} ° pessoa: "))
    sexo = str(input(f"Digite o sexo da {p} ° pessoa: "))
    print("\n")
    soma_idade += idade
    if (p == 1 and sexo in "Mm"):
        idade_max_masc = idade
        nome_old_masc = nome
    if (sexo in "mM" and idade > idade_max_masc):
        idade_max_masc = idade
        nome_old_masc = nome
    if (sexo in "fF" and idade < 20):
        menor20 += 1
media_idade_grupo = soma_idade / p
print (f"O homem mais velho do grupo é o {nome_old_masc} que tem {idade_max_masc} anos!")
print (f"A média de idade do grupo informado é de {media_idade_grupo} anos!")
print (f"Do grupo informado, {menor20} mulheres tem menos de 20 anos! ")