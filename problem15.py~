def latticePaths(x,y):
    numRows = x+y+1
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    count = 2
    triangle = [[1]]
    for i in range(1, numRows):
        current = []
        for j in range(0, count):
            if (j == 0) or (j == (count-1)):
                current.append(1)
            else:
                current.append(triangle[i-1][j-1]+triangle[i-1][j])
        triangle.append(current)
        count += 1
    return triangle[x+y][y]

print latticePaths(20,20)
