import sys
from collections import deque

input = sys.stdin.readline
Y, X = map(int,input().split())
cheese = [list(input().split()) for _ in range(Y)]
visited = [[False]*X for _ in range(Y)]
que = deque()
for y in range(Y):
    for x in range(X):
        if y==0 or y==(Y-1) or x==0 or x==(X-1):
            que.append((y,x,0))
            visited[y][x] = True
             
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def melt(que):
    now = 0
    save = 0
    while que:
        y, x, time = que.popleft()
        if now < time:
            now = time
            save = 1
        elif now == time and cheese[y][x] == '1':
            save += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= Y or nx >= X:
                continue
            if visited[ny][nx]:
                continue
            if cheese[ny][nx] == '0':
                que.appendleft((ny,nx,time))
                visited[ny][nx] = True
            elif cheese[ny][nx] == '1':
                que.append((ny,nx,time+1))
                visited[ny][nx] = True
    return time, save

a, b = melt(que)
print(a)
print(b)
            