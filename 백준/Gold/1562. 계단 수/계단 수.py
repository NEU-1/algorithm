import sys
input = sys.stdin.readline

N = int(input())

dp = [[[0] * (1 << 10) for _ in range(10)] for __ in range(N + 1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

MOD = 1000000000

for i in range(2, N + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j == 0:
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]
            elif j == 9:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
            else:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]

            dp[i][j][k | (1 << j)] %= MOD

result = 0
full_bit = (1 << 10) - 1
for i in range(10):
    result += dp[N][i][full_bit]
    result %= MOD

print(result)
