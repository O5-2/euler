import math
P = lambda i: (i*((3*i) - 1))//2
unP = lambda p: math.ceil(math.sqrt(p*2.0/3.0))
isP = lambda n: (P(unP(n)) == n)

maxD = 6000000 # Do I need to increase this number?
j = 2
while (maxD == 6000000): # Do I need to increase this number?
    for k in range(1, j):
        if (isP(P(j)+P(k)) and isP(P(j)-P(k))):
            if P(j)-P(k) < maxD:
                maxD = P(j)-P(k)
                break
    j += 1

print(maxD)
