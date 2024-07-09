num = int(input("Digite um número inteiro: "))
print("1 - Base Binária")
print("2 - Base Octal")
print("3 - Base Hexadecimal")
base = int(input("Agora escolha a base para a qual quer converter: "))
if (base == 1):
    print(f"O número {num} na base Binária é igual a {bin(num)}")
if (base == 2):
    print(f"O número {num} na base Octal é igual a {oct(num)}")
if (base == 3):
    print(f"O número {num} na base Hexadecimal é igual a {hex(num)}")
if (base != 1 and base != 2 and base != 3):
    print("Opção inválida!!! Tente novamente.")