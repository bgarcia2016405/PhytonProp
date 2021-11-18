def isPrime(num):
    for q in range(2,num):
      if num % q == 0:
        return False
    return True
   
   
#
# coloca tu código aquí
#

for i in range(1, 20):
    if isPrime(i + 1) :
        print(i + 1, end=" ")
print()
