from decimal import *

def order(a, n):
    k = 1
    aToTheK = a
    while (aToTheK % n != 1):
        aToTheK = (aToTheK*a) % n
        k += 1
    return k

Bgreatest = -1
BgreatestI = -1
for i in range(2, 1000):
    if ((i % 2 != 0) and (i % 5 != 0)):
        cur = order(10, i)
        if cur > Bgreatest:
            Bgreatest = cur
            BgreatestI = i

print(BgreatestI)
