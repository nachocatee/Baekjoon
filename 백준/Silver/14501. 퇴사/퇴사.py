N = int(input())
plan = [list(map(int, input().split())) for _ in range(N)]
# print(plan)

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + plan[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], plan[i][1] + dp[i + plan[i][0]])

print(dp[0])