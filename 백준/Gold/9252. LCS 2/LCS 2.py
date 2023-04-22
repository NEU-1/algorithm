import sys

def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp

def find_lcs(dp, s1, s2, i, j):
    if i == 0 or j == 0:
        return ""

    if s1[i - 1] == s2[j - 1]:
        return find_lcs(dp, s1, s2, i - 1, j - 1) + s1[i - 1]
    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            return find_lcs(dp, s1, s2, i - 1, j)
        else:
            return find_lcs(dp, s1, s2, i, j - 1)

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

dp = lcs(s1, s2)
lcs_str = find_lcs(dp, s1, s2, len(s1), len(s2))

print(dp[-1][-1])
print(lcs_str)

