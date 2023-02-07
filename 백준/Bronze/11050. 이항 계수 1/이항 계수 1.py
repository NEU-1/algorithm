N, K = map(int,input().split())

qube = [[1]*(N+1) for _ in range(N+1)]

for y in range(N+1):
    for x in range(N+1):
        if y >= 1 and x >= 1:
            qube[y][x] = qube[y-1][x] + qube[y][x-1]
print(qube[N-K][K])