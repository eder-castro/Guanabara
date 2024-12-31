qual = 0
while qual >= 0:
    qual = int(input("Quer ver a tabuada de qual valor? "))
    if qual < 0:
        break
    print ("-" * 36)
    n = res = 0
    while n <=10:
        print(f"{qual:<5} x {n:^5} = {res:>5}")
        n += 1
        res = qual * n
    print ("-" * 36)
print("Programa TABUADA Encerrado!")
