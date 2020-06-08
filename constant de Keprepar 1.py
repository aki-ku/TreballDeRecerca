numero = input("Dona quatre números diferents: ")
#To do Hola Jianjing, volia que fessis un parell de coses. D'una banda has de trobar tu la # constant, es a dir, el bucle s'acaba quan es torna a repetir el nombre del pas anterior, 
# tu suposes que ja la coneixes, i es tracta de que la trobis. D'altra banda m'agrdaria que
# comentis els diferents pasos explicant que fas. 
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