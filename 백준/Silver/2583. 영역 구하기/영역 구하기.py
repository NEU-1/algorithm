from collections import deque

M, N, K = map(int, input().split())

paper = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

save = []
for i in range(M):
    for j in range(N):
        if not visited[i][j] and paper[i][j] == 0:
            check = deque([(i, j)])
            visited[i][j] = True
            cnt = 1
            while check:
                x, y = check.popleft()
                for K in range(4):
                    nx, ny = x + dx[K], y + dy[K]
                    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and paper[nx][ny] == 0:
                        visited[nx][ny] = True
                        cnt += 1
                        check.append((nx, ny))
            save.append(cnt)

print(len(save))
print(' '.join(map(str, sorted(save))))
