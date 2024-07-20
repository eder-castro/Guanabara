base = int(input("Digite um numero para ver a sua tabuada: "))
print("_"*12)
for n in range (1,11):
    print ('{0:4d} x {1:4d} = {2:4d}'.format(n, base, n * base))
print("_"*12)