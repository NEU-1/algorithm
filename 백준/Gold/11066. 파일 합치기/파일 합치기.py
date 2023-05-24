import sys
T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*K for _ in range(K)]
    sum = [0]*(K+1)
    for i in range(K):
        sum[i+1] = sum[i] + files[i]
    for x in range(1, K):
        for i in range(K-x):
            dp[i][i+x] = min([dp[i][k] + dp[k+1][i+x] for k in range(i, i+x)]) + sum[i+x+1] - sum[i]
    print(dp[0][K-1])
