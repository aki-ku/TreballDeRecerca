import math
opcio = input("Digues si vols buscar la hipotenusa pulsa 0 o catet pulsa 1: ")
if opcio == "0":
  c1 = int(input("Catet 1 : "))
  c2 = int(input("Catet 2 : "))
  c = c1 **2 + c2 **2
  h = math.sqrt(c)
  print("La hipotenusa és " , h)
else:
  h = int(input("Hipotenusa: "))
  c1 = int(input("Catet 1 : "))
  c2 = h **2 - c1 **2
  c = math.sqrt(c2)
  print("El catet és " , c)