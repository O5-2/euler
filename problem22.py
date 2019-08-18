fin = open ('p022_names.txt', 'r')

names = fin.readline()

names = names.split(',')

names = [i[1:-1] for i in names]

names.sort()

sumVals = 0

for i in range(0, len(names)):
    sumVals += (i+1)*sum([ord(j)-64 for j in names[i]])

print sumVals
