from random import shuffle
al1 = input("Digite o nome do primeiro aluno: ")
al2 = input("Digite o nome do segundo aluno: ")
al3 = input("Digite o nome do terceiro aluno: ")
al4 = input("Digite o nome do quarto aluno: ")
al5 = input("Digite o nome do quinto aluno: ")
alunos = [al1, al2, al3, al4, al5]
shuffle(alunos)
print("A ordem de apresentação será {}".format(alunos))
