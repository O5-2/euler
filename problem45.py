import math
T = lambda i: (i*(i+1))//2
unT = lambda p: math.floor(math.sqrt(p*2.0))
isT = lambda n: (T(unT(n)) == n)
P = lambda i: (i*((3*i) - 1))//2
unP = lambda p: math.ceil(math.sqrt(p*2.0/3.0))
isP = lambda n: (P(unP(n)) == n)
H = lambda i: i*((2*i) - 1)
unH = lambda p: math.ceil(math.sqrt(p/2.0))
isH = lambda n: (H(unH(n)) == n)

i = 144
while not (isT(H(i)) and isP(H(i))):
    i += 1

print(H(i))
