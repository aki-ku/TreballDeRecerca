import random
print( "Benvingut al programa que tens que endevinar ")
x=random.randrange(10)
x1 = int(input("Pensi i escriu un número entre el 0 i 10 "))
if (x == x1):
    print ("Enhorabona has encertat!")
else:
    print ("Mala sort no l'ha encertat")