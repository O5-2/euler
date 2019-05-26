singles = {0: 0, 1: len("one"), 2: len("two"), 3: len("three"), 4: len("four"), 5: len("five"), 6: len("six"), 7: len("seven"), 8: len("eight"), 9: len("nine")}
teens = {10: len("ten"), 11: len("eleven"), 12: len("twelve"), 13: len("thirteen"), 14: len("fourteen"), 15: len("fifteen"), 16: len("sixteen"), 17: len("seventeen"), 18: len("eighteen"), 19: len("nineteen")}
tens = {0: 0, 2: len("twenty"), 3: len("thirty"), 4: len("forty"), 5: len("fifty"), 6: len("sixty"), 7: len("seventy"), 8: len("eighty"), 9: len("ninety")}

def numLength(num):
    tensDigit = (num // 10) % 10
    hundredsDigit = num // 100
    if num < 10:
        return singles[num]
    elif num < 100:
        if num < 20:
            return teens[num]
        else:
            return tens[tensDigit] + singles[num % 10]
    elif num < 1000:
        if num % 100 == 0:
            return singles[hundredsDigit] + 7
        else:
            return singles[hundredsDigit] + 10 + numLength(num % 100)
    else:
        return 11

def countNumbers(first, last):
    letters = 0
    for i in range(first, last+1):
        letters += numLength(i)
    return letters

print countNumbers(1, 1000)
