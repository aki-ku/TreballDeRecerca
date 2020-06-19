# Matemàtiques en la programació
En aquí us explicaré tots els programes que he fet i com funciona.

# 1. Taula de multiplicació
Com veieu el codi 1.py  
``` python3
numero = int(input("Quin número vols multiplicar: "))
print("La taula de multiplicació és: ")
for multiplicador in range(1, 11):
   print(str(numero) + "*" + str(multiplicador) + " = " + str(numero  * multiplicador))
```
