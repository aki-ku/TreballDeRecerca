import random
tiradaOrdinador = random.randrange(3)
print ("Benvingut al joc de pedra, paper i tissores")
tiradaUsuari = int(input ("Digues entre aquest dos quin vols, pedra escrius 0, paper escrius 1 o tissores escrius 2 "))
if (tiradaUsuari == 0) or (tiradaUsuari == 1) or (tiradaUsuari == 2):
  if (tiradaUsuari == tiradaOrdinador): 
    print("Has empatat")
  elif ((tiradaOrdinador == 0) and (tiradaUsuari == 1)) or ((tiradaOrdinador == 1) and (tiradaUsuari == 2)) or ((tiradaOrdinador == 2) and (tiradaUsuari == 0)):
    print("Has guanyat")
  else:
    print("Has perdut")