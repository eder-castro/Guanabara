pesos = []
for p in range (0, 5):
    peso = float(input(f"Digite o peso da {p+1}° pessoa (kg): "))
    pesos.append(peso)
print (f"O maior peso digitado foi de {max(pesos):.2f} kg!")
print (f"O menor peso digitado foi de {min(pesos):.2f} kg")