import sys

N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = 1000 * N + 1
result = INF

for first in range(3):
    dp = [[0, 0, 0] for _ in range(N)]
    for i in range(3):
        if i == first:
            dp[0][i] = costs[0][i]
        else:
            dp[0][i] = INF

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    for i in range(3):
        if i == first:
            continue
        result = min(result, dp[N-1][i])

print(result)
