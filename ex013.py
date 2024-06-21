salario_atual = float(input("Qual o salário do funcionário? "))
perc_reajuste = float(input("Qual o percentual de reajuste? "))/100
novo_salario = (salario_atual * perc_reajuste) + salario_atual
print("O novo salário é {}".format(novo_salario))