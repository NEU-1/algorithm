import sys
input = sys.stdin.readline

N = int(input())
save = [list(map(int,input().split())) for _ in range(N)]

dp = [[] for _ in range(N)]
dp[N-1] = save[N-1]
for i in range(N-1, 0, -1):
    for j in range(i):
        dp[i-1].append(max(dp[i][j], dp[i][j+1]) + save[i-1][j])
print(dp[0][0])