def ways(n, coins):
    if n == 0:
        return 1
    if len(coins) == 0:
        return 0
    ans = 0
    for i in range(0, (n // coins[-1])+1):
        ans += ways(n-(coins[-1]*i), coins[:-1])
    return ans

print(ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))
