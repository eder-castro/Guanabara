sal = float(input("Informe o salário do funcionário: R$ "))
if (sal <= 1250):
    print("Novo salário = R$ {:.2f}".format(sal * 1.15))
else:
    print("Novo salário =R$ {:.2f}".format(sal * 1.1))