valids = []
    
for n in range(1, 10000):
    multiples = ""
    i = 1
    while len(multiples) < 9:
        multiples += str(n*i)
        i += 1
    if (len(multiples) == 9) and (sorted(multiples) == [str(i) for i in range(1, 10)]):
        valids.append(int(multiples))

print(max(valids))
