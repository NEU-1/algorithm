from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[-1]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
d = [[0]*m for _ in range(n)]
group_size = []

def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    group_size.append(1)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == False and a[nx][ny] == 0:
                check[nx][ny] = True
                group[nx][ny] = cnt
                group_size[cnt] += 1
                q.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            check[i][j] = True
            bfs(i, j, cnt)
            cnt += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                    near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans%10, end='')
    print()
