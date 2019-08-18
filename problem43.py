def digitsToNum(digits):
    digits = digits[::-1]
    n = 0
    for i in range(0, len(digits)):
        n += digits[i]*(10**i)
    return n

def permuteDigits(digits):
    if len(digits) == 1:
        return [digits]
    ways = []
    for i in range(0, len(digits)):
        ways.extend([[digits[i]]+j for j in permuteDigits(digits[:i]+digits[i+1:])])
    return ways

numbers = permuteDigits([i for i in range(0, 10)])
total = 0
divisors = [2, 3, 5, 7, 11, 13, 17]

for i in numbers:
    temp = True
    for j in range(0, 7):
        if digitsToNum(i[j+1:j+4]) % divisors[j] != 0:
            temp = False
            break
    if temp:
        total += digitsToNum(i)

print(total)

# Okay, here's the problem as far as I can tell:
# There are 3628800 pandigital numbers of length 9. Three point six million.
# It's actually kind of amazing that it only takes sixty seconds or so.
