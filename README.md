# Matemàtiques en la programació

# Pràctica
En aquí us explicaré com són els programes que he fet.

## Matemàtiques

### Taula de multiplicació
Primer farem una taula de multiplicació ja que és un dels programes més fàcils que he fet que és el codi 1.py.
Com veieu el codi 1.py  
``` python3
numero = int(input("Quin número vols multiplicar: "))
print("La taula de multiplicació és: ")
for multiplicador in range(1, 11):
   print(str(numero) + "*" + str(multiplicador) + " = " + str(numero  * multiplicador))
```
Com veieu en la primera línia ens pregunta quin número vols multiplicar posem un número, la segona línia ens pinta per la pantalla la frase que està en parèntesis , la tercera ens fa un bucle de 10 vegades i diu que comença amb el 1 i acaba al 10, ja que com veiem dintre del parèntesis és 11 però li restem 1 perquè no el conta el número que li poses es com (inici, final-1)  i última línia pintas en la pantalla l’acció del bucle, és a dir,  que poses el número de la primera línia que multipliquen en el bucle i ens dóna una resposta.
 
### Equació de 2n grau
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

### Teorema de Pitàgores
El teorema de Pitàgores, en el seu enunciat habitual, estableix que en un triangle rectangle la suma dels quadrats dels catets (els costats que formen l'angle recte) és igual al quadrat de la hipotenusa (l'altre costat)
Com veiem el codi 4.py
``` python3
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
  c2 = h **2 - c2 **2
  c = math.sqrt(c2)
  print("El catet és " , c)
```
Com veiem el necessitem un import ja que és una biblioteca i la que necessitem és justament la de matemàtiques. Després volem saber si vols calcular un catet o una hipotenusa, si vols una hipotenusa pulsa 0, on preguntem els metres dels dos catets i fem la fórmula de la hipotenusa. I si pulsem 1 el que calculem és el catet que falta on preguntem la hipotenusa i el catet.

### Constant de Kaprekar
La constant de Kaprekar és una constant de quatre números que fem ordenar de més gran a més petit per fer una resta i el repetim fins que ens doni 6174 ja que si el segueixes serà el mateix resultat, hi ha dos maneres de fer-lo el codi 5.py i el codi 6.py.
Com veiem el codi 5.py
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
 
Codi 6.py
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

## Jocs

### Cara i creu
El cara o creu és un joc d'atzar entre dues parts que pronostiquen la posició en què restarà una moneda després de ser llançada a l'aire. Els dos jugadors decideixen opcions contràries entre cara o creu i, en llençar la moneda, guanya qui ha encertat quina de les dues parts ha quedat boca amunt.
Com veiem el codi 7.py.
``` python3
import random
print( "Benvingut al programa que tens que endevinar si és cara o creu d'una moneda")
x = random.randrange(2)
m1 = int(input("Abans de res tens que escollit cara o creu. Si esculls cara has d'escriure 0, i si es creu has d'escriure 1:  "))
if (0 == x) and (0 == m1):
 print ("Has guanyat i ha sortit cara ")
elif (1 == x) and (1 == m1):
 print ("Has guanyat i ha sortit creu")
else:
 print("Has perdut")
```
Primer abans de res el que fem és un import random, aquest import ens busca els números si veus en la tercera línia hem escrit que la mateixa màquina ens decideixi un número de 0 a 1, encara que em escrit fins a dos es que 0 i 1 ja són dos números. La màquina ja ha escollit ara et toca a tu escollir si vols cara o creu escrivint 0 o 1. Si ha màquina i tu heu escollit el mateix número has guanyat però si són diferents has perdut.

### Parell i senar
Parell i senars és un joc on dues o més persones amb les seves mans posen el número que decideix i vosaltres decidiu si la suma de tots és parell o senar.
Com veiem el codi 8.py.
``` python3
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
```
En aquest programa el que utilitzem és molt semblant a la de cara i creu, però la màquina decideix més números. Hem fet que la màquina digues de 0 a 10 i nosaltres també hem decidit aquest número i si és parell o senar el resultat final. Un cop fet això fa la suma de tots dos i el mòdul, és a dir el residu de la divisió. Si el residu dóna 0 és parell i si dóna 1 és senar. Després el que fa és comparar el que hem dit al principi si és parell o senar, més el mòdul.

### Pedra, paper i tisores
Normalment s'utilitza com a mètode de selecció (com també es podria fer tirant els daus, per exemple) i així triar una persona de manera aleatòria per a algun propòsit, encara que, a diferència de la selecció aleatòria, s'hi pot jugar amb habilitat si el joc es fa molt repetidament, perquè un dels jugadors pot reconèixer la tàctica no aleatòria de l'oponent.
Com veiem el cosi 9.py.
``` python3
import random
tiradaOrdinador = random.randrange(3)
print ("Benvingut al joc de pedra, paper i tissores")
tiradaUsuari = int(input ("Digues entre aquest dos quin vols, pedra escrius 0, paper escrius 1 o tissores escrius 2 "))
if (tiradaUsuari == 0) or (tiradaUsuari == 1) or (tiradaUsuari == 2):
    if (tiradaUsuari == tiÇradaOrdinador): 
        print("Has empatat")
    elif ((tiradaOrdinador == 0) and (tiradaUsuari == 1)) or ((tiradaOrdinador == 1) and (tiradaUsuari == 2)) or ((tiradaOrdinador == 2) and (tiradaUsuari == 0)):
        print("Has guanyat")
    else:
        print("Has perdut")
```
En aquest joc és com els altres dos anteriors aquest també necessita import random però només de tres números i el que fa el programa és que fa és comparar el número de la màquina amb el nostre.

### Endevina el número
En aquest joc hem de endevinar el número.
Com veiem el codi 10.py.
```python3
mport random
print( "Benvingut al programa que tens que endevinar ")
x=random.randrange(10)
x1 = int(input("Pensi i escriu un número entre el 0 i 10 "))
if (x == x1):
   print ("Enhorabona has encertat!")
else:
   print ("Mala sort no l'ha encertat")
```
En aquest joc el que fa és que la mateixa màquina decideix un número i el compara amb el que has decidit tu. Si és igual els números guanyes, però si és diferent perds.

### Endevina la paraula
En aquest joc el que fem és endevinar una palabra.
Com veiem el codi 11.py.
```python3
nom = input("Hola, benvingut al joc d'endevinar la paraula. Abans de res volem saber el teu nom : ")
paraula = "sword art online"
print("Bon dia, sr/sra " + nom )
punts = 100
opcio = 0
tiradas = 0
while (punts != 0) and (opcio != 8) and (tiradas != 5):
 print("Ara mateix tens " + str(punts) +
"""  >1. Vol saber la  posició que està una lletra? (20 punts)
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
```
En aquest joc on la línia 2 escrius la paraula que vols que se’n endevini i et dóna pistes, on tens 100 punts al principi cada pista que utilitzem gastem punts depèn de la importancia de la pista. La primera ens dóna la pista d’on estarà aquesta lletra en quina posició; la segona és la longitud de la paraula; la tercera quantes vegades apareix la lletra; la quarta si vols saber primera lletra; la cinquena si la última lletra; la sisena  se li pot mostrar només les consonants de les paraules (les vocals han d'aparèixer en *) i la setena és entrar paraula. En la primera pista com hem dit el que fa és buscar la posició de la lletra amb un for i if, justament el for fins a la longitud de la paraula i el if per poder comparar on està aquesta paraula. En la segona pista només amb un len() et diu ja la longitud de la paraula. La tercera utilitzem un nova variable per saber quantes vegades ha aparegut aquesta lletra amb la mateixa manera que la primera pista. En la quarta amb un paraula[0] sabem la primera lletra de la paraula, la cinquena amb paraula[-1] sabem la última paraula. La sisena et diu totes les consonants excepte els vocals, la setena has de escriure la resposta i l'última surts del programa. 
