print ("-" * 36)
print ("{: ^36}".format(" Sequencia de Fibonacci " ))
print ("-" * 36)
termos = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
qtd = 36
if termos > 8:
    qtd = 5 * termos + 20
print ("~" * qtd)
n = 3
print (f"{t1} => {t2}", end = '')
while (n <= termos):
    t3 = t1 + t2
    print (f" => {t3}", end = '')
    t1 = t2
    t2 = t3
    n += 1
print (" => FIM")
print ("~" * qtd)
