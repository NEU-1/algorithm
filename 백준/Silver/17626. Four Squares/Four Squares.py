import math

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i  

    for j in range(1, int(math.sqrt(i)) + 1):
        if j * j == i:
            dp[i] = 1
            break
        dp[i] = min(dp[i], dp[j*j] + dp[i-j*j])

print(dp[n])
