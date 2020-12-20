import random
print( "Benvingut al programa que tens que endevinar si és cara o creu d'una moneda") 
x = random.randrange(2)
m1 = int(input("Abans de res tens que escollit cara o creu. Si esculls cara has d'escriure 0, i si es creu has d'escriure 1: "))
if (0 == x) and (0 == m1): 
  print ("Has guanyat i ha sortit cara ") 
elif (1 == x) and (1 == m1): 
  print ("Has guanyat i ha sortit creu") 
else:
  print("Has perdut")
