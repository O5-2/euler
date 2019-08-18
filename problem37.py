from math import sqrt

def numToDigits(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n = n // 10
    return digits

def digitsToNum(digits):
    n = 0
    for i in range(0, len(digits)):
        n += digits[i]*(10**i)
    return n

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

def isTruncatablePrime(x):
    if not isPrime(x):
        return False
    if (x < 10):
        return True
    a = x+0
    b = x+0
    while len(numToDigits(a)) != 0:
        a = digitsToNum(numToDigits(a)[:-1])
        b = b // 10
        if not (isPrime(a) and isPrime(b)):
            return False
    return True

def increment(i):
    digits = numToDigits(i+2)
    for j in range(0, len(digits)):
        if (digits[j] % 2 != 1) and (j == 0 and digits[j] == 2):
            digits[j] += 1
    return digitsToNum(digits)

valids = []
i = 11

while len(valids) < 11:
    if isTruncatablePrime(i):
        valids.append(i)
    i = increment(i)

print(sum(valids))
