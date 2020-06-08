numero = int(input("Dona quatre números diferents: "))

resposta = 0

while(resposta != 6174):

  numero2 = numero // 1000
  numero3 = numero2 // 100
  numero4 = numero3 // 10
  numero5 = numero4 // 1
  
  print(str(numero2) + "/" + "1000 =" str(numero // 1000) )
  print(str(numero3) + "/" + "100 =" str(numero2 // 100) )
  print(str(numero4) + "/" + "10 =" str(numero3 // 10) )
  print(str(numero5) + "/" + "1 =" str(numero4 // 1) )
 
  llistes = []
  llistes = llistes + numero2 + numero3 + numero4 + numero5
  llistes2 = []
  llistes2 = llistes2 + numero2 + numero3 + numero4 + numero5

  
  print(llistes, llistes2)