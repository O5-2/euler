from math import sqrt

def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    root = int(sqrt(x)) + 1
    for i in range(2, root+1):
        if x % i == 0:
            return False
    return True

def numPrimeDivisors(num):
    if isPrime(num):
        return 1 # Not quite true, but makes things easier
    for i in range(2, num//2 +1):
        if num % i == 0:
            while num % i == 0:
                num = num // i
            return 1+numPrimeDivisors(num)
    return 0

i = 5
d = {i: numPrimeDivisors(i), i+1: numPrimeDivisors(i+1), i+2: numPrimeDivisors(i+2), i+3: numPrimeDivisors(i+3)}
while [d[j] for j in range(i, i+4)] != [4, 4, 4, 4]:
    d[i+4] = numPrimeDivisors(i+4)
    i += 1

print(i)
