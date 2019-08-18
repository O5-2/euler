from math import sqrt

def arrayAnd(bools):
    for i in bools:
        if not i:
            return False
    return True

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

def rotateDigits(digits):
    ways = []
    for i in range(0, len(digits)):
        ways.append(digits[i:]+digits[:i])
    return ways

def isPrime(x):
    root = int(sqrt(x)) + 1
    for i in range(2, root+1):
        if x % i == 0:
            return False
    return True

valids = [2, 3, 5, 7]

for i in range(10, 1000001):
    if arrayAnd([isPrime(digitsToNum(j)) for j in rotateDigits(numToDigits(i))]):
        valids.append(i)
        
print(len(valids))
