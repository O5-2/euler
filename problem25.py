from math import sqrt
from decimal import *

def NthFibonacci(n):
    plusPhi = (Decimal(1)+Decimal(sqrt(Decimal(5))))/Decimal(2)
    minusPhi = (Decimal(1)-Decimal(sqrt(Decimal(5))))/Decimal(2)
    a = plusPhi**n
    b = minusPhi**n
    z = (a-b)/Decimal(sqrt(Decimal(5)))
    return z

n = 0

while NthFibonacci(n) < 10**999:
    n += 1

print(n)
