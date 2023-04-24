import sys

input = sys.stdin.readline

# 입력받기
N = int(input().strip())
seq = list(map(int, input().strip().split()))
M = int(input().strip())

# 다이나믹 프로그래밍 테이블 초기화
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 길이가 1인 팰린드롬 초기화
for i in range(1, N + 1):
    dp[i][i] = 1

# 길이가 2인 팰린드롬 초기화
for i in range(1, N):
    if seq[i - 1] == seq[i]:
        dp[i][i + 1] = 1

# 길이가 3 이상인 팰린드롬 검사
for k in range(2, N):
    for i in range(1, N - k + 1):
        j = i + k
        if seq[i - 1] == seq[j - 1] and dp[i + 1][j - 1]:
            dp[i][j] = 1

# 쿼리 처리
for _ in range(M):
    s, e = map(int, input().strip().split())
    print(dp[s][e])
