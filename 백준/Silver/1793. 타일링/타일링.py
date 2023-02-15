def tile(n):
    dp = [1, 1, 3]
    for i in range(3, n+1):
        dp.append(dp[i-2] * 2 + dp[i-1])
    return dp[n]

while True:
    try:
        n = int(input())
        print(tile(n))
    except EOFError:
        break