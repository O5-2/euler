def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)

def lexPerm(n, chars):
    decider = lambda x, y: y[0]+y[1] if (x == 1) else y[1]+y[0]
    if len(chars) == 1:
        return chars[0]
    if len(chars) == 2:
        return decider(n, chars)
    if n <= 1:
        return ''.join(chars)
    specialModulo = lambda x, y: y if (x % y == 0) else x % y
    specialDivide = lambda x, y: (x/y)-1 if (x % y == 0) else x/y
    a = factorial(len(chars)-1)
    b = specialModulo(n, a)
    c = specialDivide(n, a)
    return chars[c]+lexPerm(b, chars[:c]+chars[c+1:])

print lexPerm(1000000, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
