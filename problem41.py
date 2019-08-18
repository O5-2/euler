from math import sqrt

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

def permuteDigits(digits):
    if len(digits) == 1:
        return [digits]
    ways = []
    for i in range(0, len(digits)):
        ways.extend([[digits[i]]+j for j in permuteDigits(digits[:i]+digits[i+1:])])
    return ways

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

m = 0
for i in range(2, 10):
    d = [j for j in range(1, i+1)]
    for j in permuteDigits(d):
        if (digitsToNum(j) > m) and (isPrime(digitsToNum(j))):
            m = digitsToNum(j)
    print(m)
    print("//")

print(m)

# Okay, here's the problem as far as I can tell:
# There are 362880 pandigital numbers of length 9. (a 9x increase from length 8)
# Each of them is somewhere between 100 million and 1000 million. (a 10x increase from length 8)
# Since my prime-testing function takes about O(n^1/2) time (maybe?), that's an increase of 3x or so from length 8.
# Multiply together, and we get an increase of 270x at least.
# Even though length 8 only takes a few seconds, that means a good chunk of an hour for length 9.

# It turns out that there are no pandigital primes of length 9 for whatever reason, though, which makes the thing moot.
