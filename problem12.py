from math import sqrt

def numDivisors(num):
    if num == 1:
        return 1
    divisors = 1
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            while num%i == 0:
                divisors += 1
                num /= i
            break
    if divisors == 1:
        return 2
    return divisors*numDivisors(num)

def triangleDivisors(atLeast):
    current = 3
    count = 3
    while True:
        current += count
        divisors = numDivisors(current) #2
        #for i in range(2,int(sqrt(current))+1):
        #    if current % i == 0:
        #        divisors += 2
        if divisors >= atLeast:
            return current
        count += 1

print triangleDivisors(500)
