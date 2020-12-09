# Matemàtiques en la programació

# Pràctica
En aquí us explicaré com són els programes que he fet.

## Taula de multiplicació
Primer farem una taula de multiplicació ja que és un dels programes més fàcils que he fet que és el codi 1.py.
Com veieu el codi 1.py  
``` python3
numero = int(input("Quin número vols multiplicar: "))
print("La taula de multiplicació és: ")
for multiplicador in range(1, 11):
   print(str(numero) + "*" + str(multiplicador) + " = " + str(numero  * multiplicador))
```
Com veieu en la primera línia ens pregunta quin número vols multiplicar posem un número, la segona línia ens pinta per la pantalla la frase que està en parèntesis , la tercera ens fa un bucle de 10 vegades i diu que comença amb el 1 i acaba al 10, ja que com veiem dintre del parèntesis és 11 però li restem 1 perquè no el conta el número que li poses es com (inici, final-1)  i última línia pintas en la pantalla l’acció del bucle, és a dir,  que poses el número de la primera línia que multipliquen en el bucle i ens dóna una resposta.
 
## Equació de 2n grau
Com sabem hi ha dos tipus d’equacions de 2n grau, la que donà una resposta real que és el codi 2.py i la que donà una resposta imaginària que és el codi 3.py.
Com veieu el codi 2.py  
```python3
import math
print ("a*x^2+bx+c=0")
a = float(input("valor a: "))
b = float(input("valor b: "))
c = float(input("valor c: "))
if ((b**2 - 4*a*c)< 0):
   print ("Error/ No hi ha solució en els nombres reals")
else:
   print("A continuació la solució")
   print ((-b+ math.sqrt(b**2 - (4*a*c)))/(2*a))
   print ((-b- math.sqrt(b**2 - (4*a*c)))/(2*a))
```
Com veiem en la primera línia utilitzem un import math que és una biblioteca plena d’operacions matemàtiques, en la segona línia pintem com serà la nostra condició, és a dir, com ho tenim que la suma del total és igual a 0, la tercera, quarta i cinquena línia volem saber quins són els tres valors que tenim. La sisena i la vuitena és per parla sobre la condició, la sisena diu que si l'arrel quadrada és menor que 0, ja significa que no pot tenir, i en la següent línia pinta que és un error, mentre tant la vuitena línia diu sinó de la condició i fa els següents càlculs.
 
Com veiem en el codi 3.py.
```python3
import math
print ("a*x^2+bx+c=0")
a = float(input("valor a: "))
b = float(input("valor b: "))
c = float(input("valor c: "))
if ((b**2 - 4*a*c)< 0):
   print (str(- b + math.sqrt((b**2 - (4*a*c)) * -1) /(2*a)) + "j")
   print (str(- b - math.sqrt((b**2 - (4*a*c)) * -1) /(2*a)) + "j")
else:
   print("A continuació la solució")
   print ((-b+ math.sqrt(b**2 - (4*a*c)))/(2*a))
   print ((-b- math.sqrt(b**2 - (4*a*c)))/(2*a))
```
Com veiem en aquest programa es igual que el 3.py que només afegim unes operacions més que és la dels números imaginaris ja com en la sisena línia ens parla d’una operació impossible així multipliquem per -1, que els operacions estan en la setena i vuitena línia i al final té una j que significa números complexos.
 
## Constant de Kaprekar
La constant de Kaprekar és una constant de quatre números que fem ordenar de més gran a més petit per fer una resta i el repetim fins que ens doni 6174 ja que si el segueixes serà el mateix resultat, hi ha dos maneres de fer-lo el codi 4.py i el codi 5.py.
Com veiem el codi 4.py
``` python3
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
```
Com veiem en la primera línia ens pregunta quatre números diferents, 
l’escrivim, en la segona línia escrivim que la resposta és igual que zero, per 
donar una idea per la següent línia, és a dir, la tercera línia és un bucle (while) que no s’acaba fins que la resposta no doni 6174. La quarta i cinquena línia faig llistes. La sisena i la setena línia és una cadena buida, la vuitena línia és una constant que està igual a zero. Desprès faig un altre bucle (for) les mateixa extensió que té el número. Aquests números els afegeix en les llistes de la onzena i dotzena línia, en la línia trezena línia es un contador per veure quantes vegades ha fet aquesta operació. Desprès fem un bucle en la línia catorzena fins a setzena, es que si el contador és diferent a quatre té que afegir un zero a les dues llistes. A continuació fem dos bucles (for), que sumen a la cadena gran que és el primer més gran de la llista i en la següent línia en l’elimina i en la cadena petit també fa el mateix però contrari que primer suma el més petit de la llista i l’elimina. Posem que el resultat és la resta del gran menys petit, el pintem per la pantalla i posem que resultat és igual que resultat i mira si resulta és igual a resultat, que és 6174, si no ho és segueix amb el bucle fins que sigui aquell número.
 
Codi 5.py
```python3
def asc(n):
 return int(''.join(sorted(str(n))))
def desc(n):
 return int(''.join(sorted(str(n))[::-1]))
n = input("Un número: ")
while n != desc(n) - asc(n):
   print (desc(n), "-", asc(n), "=", desc(n)-asc(n))
   n = desc(n) - asc(n)
print (" Resposta Kaprekar: ", n)
```
Aquest programa és més curt que l’anterior però el que utilitzem són funcions.
En la primera funció que ens dóna del més gran a més petit i en la segona funció fa el revés de més petit a més gran.  I després amb un while  fem que la resposta sigui igual a la resposta.