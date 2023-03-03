import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int,input().split())
maze = [list(input()) for _ in range(N)]
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
# print(maze)
# print(visited)
visited[0][0][0] = True
que = deque()
que.append((0,0,0,1))

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def run(que):
    while que:
        y, x, wall, cnt = que.popleft()
        # print(y, x, cnt, wall)
        if y == N-1 and x == M-1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if visited[ny][nx][0] and visited[ny][nx][1]:
                continue
            if maze[ny][nx] == '0':
                if wall == 1 and not visited[ny][nx][1]:
                    que.append((ny,nx,1,cnt+1))
                    visited[ny][nx][1] = True
                elif wall == 0 and not visited[ny][nx][0]:
                    que.append((ny,nx,0,cnt+1))
                    visited[ny][nx][0] = True
            else:
                if wall == 1:
                    continue
                elif wall == 0 and not visited[ny][nx][0]:
                    que.append((ny,nx,1,cnt+1))
                    visited[ny][nx][1] = True
    return -1

print(run(que))

'''
5 8
01000000
01010000
01010000
01010011
00010010
'''