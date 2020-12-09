def asc(n):
  return int(''.join(sorted(str(n))))

def desc(n):
  return int(''.join(sorted(str(n))[::-1]))

n = input("Un número: ")

while n != desc(n) - asc(n):
    print (desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

print (" Resposta Kaprekar: ", n)