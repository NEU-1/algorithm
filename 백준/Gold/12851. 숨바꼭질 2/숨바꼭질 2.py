from collections import deque

MAX = 100001

N, K = map(int, input().split())

A = [-1] * MAX
B = [0] * MAX

q = deque()
q.append(N)
A[N] = 0
B[N] = 1

while q:
    x = q.popleft()
    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < MAX:
            if A[nx] == -1:
                A[nx] = A[x] + 1
                B[nx] = B[x]
                q.append(nx)
            elif A[nx] == A[x] + 1:
                B[nx] += B[x]

print(A[K])
print(B[K])
