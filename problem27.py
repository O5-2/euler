from math import sqrt


def isPrime(x):
    root = int(sqrt(x)) + 1
    for i in range(2, root+1):
        if x % i == 0:
            return False
    return True

most = 0
mostA = 0
mostB = 0

decider = lambda x, y, z: isPrime((x**2)+(y*x)+z) if (((x**2)+(y*x)+z) >= 0) else False

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while decider(n, a, b):
            n += 1
        if n > most:
            most = n
            mostA = a
            mostB = b

print(mostA*mostB)
