def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

valids = 0

for i in range(10, 2540161):
    I = i+0
    A = []
    while I != 0:
        A.append(I % 10)
        I = I // 10
    B = [factorial(j) for j in A]
    if i == sum(B):
        valids += i

print(valids)
        
# 9! is 362880. That has 6 digits.
# 9! times 6 is 2177280. That has 7 digits.
# 9! times 7 is 2540160. That has 7 digits.
# So we only need to check up to 2540160 inclusive. (Probably less, but *shrug*)
