import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def move(current, visited):
    if visited == (1 << N) - 1:
        if W[current][0] > 0:
            return W[current][0]
        return sys.maxsize

    if dp[current][visited] != -1:
        return dp[current][visited]

    min_value = sys.maxsize
    for i in range(1, N):
        if not visited & (1 << i) and W[current][i] > 0:
            min_value = min(min_value, W[current][i] + move(i, visited | (1 << i)))

    dp[current][visited] = min_value
    return min_value

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]

print(move(0, 1))
