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

def permuteDigits(digits):
    if len(digits) == 1:
        return [digits]
    ways = []
    for i in range(0, len(digits)):
        ways.extend([[digits[i]]+j for j in permuteDigits(digits[:i]+digits[i+1:])])
    return ways

for i in range(1000, 9998):
    permutations = [int("".join([str(m) for m in n])) for n in permuteDigits([c for c in str(i)])]
    for j in permutations:
        if i == j:
            continue
        k = i+(2*(j-i))
        if (j < 1000) or (k < 1000):
            continue
        if k <= j:
            continue
        if k not in permutations:
            continue
        if not ((isPrime(i) and isPrime(j)) and isPrime(k)):
            continue
        print(int(str(i)+str(j)+str(k)))
