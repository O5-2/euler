lengths = {1: 1}

largestD = 0
def collatzLength(num,depth):
    global largestD
    if depth > largestD:
        largestD = depth
    if num not in lengths:
        if num % 2 == 0:
            current = collatzLength(num/2,depth+1)+1
        else:
            current = collatzLength((num*3)+1,depth+1)+1
        lengths[num] = current
    else:
        x = 0
    return lengths[num]

largest = 0
for i in range(1,1000000):
    collatzI = collatzLength(i,1)
    if largest < collatzI:
        largest = collatzI
        largest_i = i
print largest_i
