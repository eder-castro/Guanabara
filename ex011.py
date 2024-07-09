alt = float(input("Medida da altura da parede: "))
larg = float(input("Medida da largura da parede: "))
rend = 2
area = alt*larg
qt_tinta = area/rend
print("Voce vai usar {:.2f} litros de tinta para pintar sua parede de {} x {}".format(qt_tinta,alt,larg))