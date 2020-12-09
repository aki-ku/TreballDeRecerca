numero = input("Dona quatre números diferents: ")

resposta = 0

while(resposta != 6174):
  
  llistes = []
  llistes2 = []
  gran = ""
  petit = ""

  cont = 0

  for i in numero:
    print(i)
    llistes.append((i))
    llistes2.append((i))
    cont = cont + 1
  
  if cont != 4:
    llistes.append("0")
    llistes2.append("0")

  for i in range(4):
    gran = gran + max(llistes)
    llistes.remove(max(llistes))

  for i in range(4):
    petit = petit + min(llistes2)
    llistes2.remove(min(llistes2))

  resultat = int(gran) - int(petit)

  print(gran, "-", petit, "=", resultat)

  numero = str(resultat)

  resposta = resultat 
  ##