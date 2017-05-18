def sumDigits(num):
    digits = [int(i) for i in str(num)]
    return sum(digits)

print sumDigits(2**1000)
