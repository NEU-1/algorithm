N, S = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(1, 1 << N):
    total = 0
    for j in range(N):
        if i & (1 << j):
            total += A[j]
    if total == S:
        cnt += 1

print(cnt)
