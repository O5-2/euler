validsSum = 0

#print(1**5 + 5**5 + 6**5 + 2**5 + 5**5)
#print(1**5 + 9**5 + 6**5 + 6**5 + 0**5 + 8**5)

#digitPowerSum = 0
#i1 = 15625
#while i1 != 0:
#    digitPowerSum += (i % 10)**5
#    i1 = i1 // 10
#if digitPowerSum == i:
#    validsSum += i

for i in range(10, 1000000):
    digitPowerSum = 0
    i1 = i
    while i1 != 0:
        digitPowerSum += (i1 % 10)**5
        i1 = i1 // 10
    if digitPowerSum == i:
        validsSum += i
        
print(validsSum)
