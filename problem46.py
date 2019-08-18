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

def isGoldbach(n):
    if isPrime(n):
        return True # Mathematically speaking, this isn't quite right, but it makes the program smoother.
    for i in range(1, int(sqrt(n/2))+1):
        if isPrime(n - 2*i*i):
            return True
    return False

i = 9
while isGoldbach(i):
    i += 2

print(i)
