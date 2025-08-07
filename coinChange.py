def getWays(n, c):
    ways = [0] * (n + 1)
    ways[0] = 1
    for coin in c:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
    return ways[n]