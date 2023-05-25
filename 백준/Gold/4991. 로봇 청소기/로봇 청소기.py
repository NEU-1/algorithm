import sys
from heapq import heappop, heappush
from itertools import permutations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
INF = float('inf')

def bfs(sx, sy):
    dist = [[-1]*w for _ in range(h)]
    q = [(sx, sy)]
    dist[sx][sy] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and room[nx][ny] != 'x' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    room, dirty = [], []
    for i in range(h):
        row = list(sys.stdin.readline().strip())
        room.append(row)
        for j in range(w):
            if row[j] == 'o':
                sx, sy = i, j
            elif row[j] == '*':
                dirty.append((i, j))

    dirty.insert(0, (sx, sy))
    n = len(dirty)
    adj = [[0]*n for _ in range(n)]
    impossible = False

    for i in range(n):
        dist = bfs(dirty[i][0], dirty[i][1])
        for j in range(i+1, n):
            if dist[dirty[j][0]][dirty[j][1]] == -1:
                impossible = True
                break
            adj[i][j] = adj[j][i] = dist[dirty[j][0]][dirty[j][1]]
        if impossible:
            break

    if impossible:
        print(-1)
        continue

    order = list(permutations(range(1, n)))
    answer = INF
    for o in order:
        temp = adj[0][o[0]]
        for i in range(n-2):
            temp += adj[o[i]][o[i+1]]
        answer = min(answer, temp)
    print(answer)
