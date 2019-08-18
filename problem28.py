nums = [[1]]

direction = 0

for i in range(1, 1001):
    if direction == 0:
        for j in range(0, i):
            nums[j] = nums[j] + [i*i + j+1]
        nums = nums + [[(i**2)+i+j+1 for j in range(i, -1, -1)]]
    elif direction == 1:
        for j in range(0, i):
            nums[i-1-j] = [i*i + j+1] + nums[i-1-j]
        nums = [[(i**2)+i+j+1 for j in range(0, i+1)]] + nums
    direction = (direction+1)%2
            
print(sum([nums[i][i] for i in range(0, 1001)])+sum([nums[i][1000-i] for i in range(0, 1001)])-nums[500][500])
