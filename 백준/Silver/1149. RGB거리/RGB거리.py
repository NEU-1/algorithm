import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
dp = [[] for _ in range(N)]
dp[0] = cost[0]
for i in range(1,N):
    for j in range(3):
        dp[i].append(min(dp[i-1][j-1],dp[i-1][j-2]) + cost[i][j])
print(min(dp[N-1]))