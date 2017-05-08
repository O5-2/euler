from math import sqrt

def triangleDivisors(atLeast):
    current = 3
    count = 3
    while True:
        divisors = 2
        current += count
        for i in range(2,int(sqrt(current))+1):
            if current % i == 0:
                divisors += 2
        if divisors >= atLeast:
            return current
        count += 1

print triangleDivisors(500)
