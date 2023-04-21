import sys

n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

max_cost = sum(cost)
dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(max_cost + 1):
        if j < cost[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memory[i - 1])

for i in range(max_cost + 1):
    if dp[n][i] >= m:
        print(i)
        break
