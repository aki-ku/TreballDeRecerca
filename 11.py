nom = input("Hola, benvingut al joc d'endevinar la paraula. Abans de res volem saber el teu nom : ")
paraula = "sword art online"
print("Bon dia, sr/sra " + nom )
punts = 100
opcio = 0
tiradas = 0
while (punts != 0) and (opcio != 8) and (tiradas != 5):
  print("Ara mateix tens " + str(punts) +
"""  
>1. Vol saber la  posició que està una lletra? (20 punts)
>2. Vol saber la longitut de la paraula? (20 punts)
>3. Se li pot dir quantes vegades apareix una lletra.  QUina lletra vols saber? (20 punts)
>4. Vol saber primera lletra? (20 punts)
>5. Vol saber la última lletra? (20 punts)
>6. Se li pot mostrar només les consonants de les paraules (les vocals han d'aparèixer en *). Aquesta superpista. Sol es pot demanar si ja s'ha intentat entrar alguna paraula. (40 punts).
>7. Entrar paraula
>8. Sortir""")  
  opcio = int(input("Quina opció tries: "))
  if (opcio == 1):  
    punts = punts - 20
    letra= input("Digues quina letra vols saber la posició: ")    
    for posicio in range(0, len(paraula)):
      if (paraula[posicio] == letra):                    
        print("Hi ha en la posició " + str(posicio + 1) + " aquesta lletra")
  elif (opcio == 2):
    punts = punts - 20
    print("Són uns " + str(len(paraula)) + " lletres")
  elif (opcio == 3):      
    punts = punts - 20
    acum = 0
    letra1 = input("Digues quina letra vols saber la posició: ") 
    for vegades in range(0, len(paraula)):
      if ( paraula[vegades] == letra1):
        acum = acum + 1
        print("Hi apareix  " + str(acum) + " vegades")
  elif (opcio == 4):
    punts = punts - 20
    print ("La primera paraula és: " + str(paraula[0]))
  elif (opcio == 5):
    punts = punts - 20
    print("La última paraula és: " + str(paraula[-1]))
  elif (opcio == 6):
    punts = punts - 40
    nouparaula = paraula.replace("a", "*")
    nouparaula = nouparaula.replace("e", "*")
    nouparaula = nouparaula.replace("i", "*")
    nouparaula = nouparaula.replace("o", "*")
    nouparaula = nouparaula.replace("u", "*")
    print(nouparaula)
  elif (opcio == 7):
    punts = punts - 15
    resposta = input("Entra la teva resposta: ")
    if (resposta == paraula):
      print ("La teva resposta és correcte !!!")
    else:
      print("Ooooh, quina mala sort...")
  else:
     break
  tiradas = tiradas + 1