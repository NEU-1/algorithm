N = int(input())
A = list(map(int, input().split()))

dp1 = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)

dp2 = [1] * N
for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)

answer = 0
for i in range(N):
    answer = max(answer, dp1[i] + dp2[i])

print(answer - 1)
