'''
9 mirim
14 infantil
19 junior
25 senior
master
'''
from datetime import date
nasc = int(input("Ano de nascimento do atleta: "))
idade = date.today().year - nasc
print (f"O atleta tem {idade} anos!")
if (idade <= 9):
    cat = 'mirim'
elif (idade <= 14):
    cat = 'infantil'
elif (idade <= 19):
    cat = 'junior'
elif (idade <= 25):
    cat = 'senior'
else:
    cat = 'master'
print (f"A categoria do atleta é {cat.upper()}!")
