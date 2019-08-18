def isPalindrome(s):
    return (s == s[::-1])

valids = 0
    
for i in range(1, 1000000):
    if (isPalindrome(str(i)) and isPalindrome(bin(i)[2:])):
        valids += i

print(valids)
