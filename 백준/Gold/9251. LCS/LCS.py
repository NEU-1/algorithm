import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())
# print(word1, word2)
dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
# print(dp)
for i in range(len(word1)):
    for j in range(len(word2)):
        if i==0 or j==0:
            dp[i][j] = 0
        if word1[i] == word2[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
# print(dp)
print(dp[-1][-1])
        