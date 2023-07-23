N = int(input())
number = list(map(int,input().split()))
M = int(input())

dp = [0 for _ in range(M+1)]

for i in range(N-1, -1, -1):
    cost = number[i]
    for j in range(cost,M+1):
        dp[j] = max(dp[j], dp[j-cost]*10 + i)
print(dp[j])