lengths = {1: 1}

def collatzLength(num):
    if num not in lengths:
        if num % 2 == 0:
            current = collatzLength(num/2)+1
        else:
            current = collatzLength((num*3)+1)+1
        lengths[num] = current
    return lengths[num]

largest = 0
for i in range(1,1000000):
    if largest < collatzLength(i):
        largest = collatzLength(i)
        largest_i = i
print largest_i
