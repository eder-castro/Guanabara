from time import sleep
vlr1 = int(input("Digite o primeiro valor: "))
vlr2 = int(input("Digite o segundo valor: "))
opc = 0
res = 0
while (opc != 5):
    print('''    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Alterar números
    [ 5 ] - Sair''')
    opc = int(input(">>>>> Escolha uma opção <<<<< \n"))
    if (opc == 1):
        res = vlr1 + vlr2
        print ("-==" * 15)
        print (f"A soma de {vlr1} e {vlr2} é {res}!")
    elif (opc == 2):
        res = vlr1 * vlr2
        print ("-==" * 15)
        print(f"A multiplicação de {vlr1} por {vlr2} é {res}!")
    elif (opc == 3):
        if (vlr1 > vlr2):
            print ("-==" * 15)
            print (f"O maior valor é {vlr1}!")
        else:
            print ("-==" * 15)
            print(f"O maior valor é {vlr2}!")
    elif (opc == 4):
        print ("-==" * 15)
        vlr1 = int(input("Digite novamente o primeiro valor: "))
        vlr2 = int(input("Digite novamente o segundo valor: "))
    elif (opc == 5):
        print ("-==" * 15)
        print ("Saindo...")
    else:
        print ("-==" * 15)
        print ("Opção Inválida!!!")
    print ("-==" * 15)
    sleep (1)
print ("Fim")

