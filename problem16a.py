def sumDigits(num):
    ans = 0
    while num != 0:
        ans += num % 10
        num //= 10
    return ans

print sumDigits(2**1000)
