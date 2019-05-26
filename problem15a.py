def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

def latticePaths(x,y):
    factorials = [1]
    for i in range(1, x+y+1):
        factorials.append(factorials[-1]*i)
    #numRows = x+y+1
    #if numRows == 0:
    #    return []
    #if numRows == 1:
    #    return [[1]]
    #count = 2
    #triangle = [[1]]
    #for i in range(1, numRows):
    #    current = []
    #    for j in range(0, count):
    #        if (j == 0) or (j == (count-1)):
    #            current.append(1)
    #        else:
    #            current.append(triangle[i-1][j-1]+triangle[i-1][j])
    #    triangle.append(current)
    #    count += 1
    #return triangle[x+y][y]
    return factorials[x+y]/(factorials[x]*factorials[y])

print latticePaths(20,20)
