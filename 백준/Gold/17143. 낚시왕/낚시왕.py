import sys
from collections import deque

input = sys.stdin.readline

R, C, M = map(int, input().split())
dx = [-1, 1, 0, 0]  # 상, 하, 우, 좌
dy = [0, 0, 1, -1]  # 상, 하, 우, 좌
sharks = deque()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r-1, c-1, s, d-1, z])

board = [[0]*C for _ in range(R)]
for shark in sharks:
    x, y, _, _, z = shark
    board[x][y] = z

answer = 0
for y in range(C):
    for x in range(R):
        if board[x][y] > 0:
            answer += board[x][y]
            board[x][y] = 0
            break
    next_board = [[0]*C for _ in range(R)]
    temp_sharks = deque()
    while sharks:
        x, y, s, d, z = sharks.popleft()
        if board[x][y] == z:
            nx, ny, nd = x, y, d
            for _ in range(s):
                nx, ny = nx+dx[nd], ny+dy[nd]
                if 0 <= nx < R and 0 <= ny < C:
                    continue
                else:
                    nx, ny = nx-dx[nd], ny-dy[nd]
                    if nd == 0:
                        nd = 1
                    elif nd == 1:
                        nd = 0
                    elif nd == 2:
                        nd = 3
                    elif nd == 3:
                        nd = 2
                    nx, ny = nx+dx[nd], ny+dy[nd]
            temp_sharks.append([nx, ny, s, nd, z])
    while temp_sharks:
        x, y, s, d, z = temp_sharks.pop()
        if not next_board[x][y] or next_board[x][y] < z:
            next_board[x][y] = z
            sharks.append([x, y, s, d, z])
    board = next_board
print(answer)
