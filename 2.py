import math

print ("a*x^2+bx+c=0")

a = float(input("valor a: "))
b = float(input("valor b: "))
c = float(input("valor c: "))

if ((b**2 - 4*a*c)< 0):
    print ("Error/ No hi ha solució")

else:
    print("A continuació la solució")
    print ((-b+ math.sqrt(b**2 - (4*a*c)))/(2*a))
    print ((-b- math.sqrt(b**2 - (4*a*c)))/(2*a))
