dp = [[0] * 41 for _ in range(2)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1
for d in range(2, 41):
    dp[0][d] = dp[0][d-1] + dp[0][d-2]
    dp[1][d] = dp[1][d-1] + dp[1][d-2]

for _ in range(int(input())):
    num = int(input())
    print(dp[0][num], dp[1][num])

 
