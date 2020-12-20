import random
import sys
print ("Benvingut al joc de parells i senars")
x = random.randrange(11)
x0 = input ("Digues entre aquest dos quin vols, parell o senar: ")
x3 = "senar"
x4 = "parell"
if (x0 == x3) or (x0 == x4):
  x1 = int(input ("Posa un número entre 0 fins al 10: "))
  x2 = (x + x1) % 2
  print (x)
  if ((x2 == 0) and (x0 == x4)) or ((x2 == 1) and (x0 == x3)):
    print ("Has guanyat")
  else:
    print("Has perdut")