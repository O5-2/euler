from math import sqrt

def divisors(num):
    if num == 1:
        return [1]
    divs = [1]
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            divs.append(i)
            divs.append(int(num/i))
    if divs == [1]:
        return [1, num]
    divs.append(num)
    return divs

def isAmicable(x):
    return (sum(divisors(sum(divisors(x)[:-1]))[:-1]) == x) and (sum(divisors(x)[:-1]) != x)

nums = 0

for i in range(2, 10001):
    if isAmicable(i):
        nums += i

print nums
