from collections import deque
import sys
input = sys.stdin.readline

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] == "O":
                continue
            if board[nrx][nry] == "O":
                print(depth)
                return
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth+1))
    print(-1)

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i, j
        elif board[i][j] == "B":
            bx, by = i, j

q = deque()
visited = set()
q.append((rx, ry, bx, by, 1))
visited.add((rx, ry, bx, by))
bfs()
