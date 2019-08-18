from math import sqrt

def divisors(num):
    if num == 1:
        return [1]
    divs = [1]
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            while num%i == 0:
                divs.append(divs[-1]*i)
                num /= i
            break
    if divs == [1]:
        return [1, num]
    ans = []
    for i in divs:
        ans += [i*j for j in divisors(num)]
    return ans

def isAbundant(x):
    return sum(divisors(x)[:-1]) > x

abundants = set()

for i in range(2, 28125):
    if (i % 2 == 0) or (i % 3 == 0):
        if isAbundant(i):
            abundants.add(i)
            
ans = 0

for i in range(1, 28125):
    able = False
    for j in abundants:
        if i-j in abundants:
            able = True
            break
    if not able:
        ans += i

print ans
