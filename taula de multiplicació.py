numero = int(input("Quin número vols multiplicar: "))
print("La taula de multiplicació és: ")
for multiplicador in range(1, 11):
    print(str(numero) + "*" + str(multiplicador) + " = " + str(numero  * multiplicador))