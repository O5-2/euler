maxSolutions = 0
maxP = -1

primitiveTriples = []
for m in range(3, 47, 2):
    for n in range(1, m, 2):
        primitiveTriples.append([m*n, (m*m - n*n)/2, (m*m + n*n)/2])

for p in range(12, 1000):
    valids = 0
    for i in primitiveTriples:
        if (p % sum(i)) == 0:
            valids += 1
    if valids > maxSolutions:
        maxSolutions = valids
        maxP = p

print(maxP)
