fin = open ('p042_words.txt', 'r')

words = fin.readline()

words = words.split(',')

words = [i[1:-1] for i in words]

words.sort()

triangleNumbers = set([1])
m = 1
i = 2

while (m < 442000):
    triangleNumbers.add(m+i)
    m += i
    i += 1

triangleWords = 0

for i in range(0, len(words)):
    sumVals = sum([ord(j)-64 for j in words[i]])
    if sumVals in triangleNumbers:
        triangleWords += 1

print(triangleWords)
