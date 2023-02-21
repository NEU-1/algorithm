from collections import deque

y_, x_ = map(int,input().split())
maze = [list(str(input()))for _ in range(y_)]
# print(maze)

run = deque()
run.append((0,0,0))
maze[0][0] = 0

dy = [1,0,-1,0]
dx = [0,1,0,-1]
cnt = 0

while run:
    # print(run)
    now = run.popleft()
    # print(now)
    y, x, dps = now
    if y == y_-1 and x == x_-1:
        cnt = dps
        break
        
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= y_ or nx >= x_:
            continue
        elif maze[ny][nx] == '1':
            # print(1111)
            # print(ny,nx)
            run.append((ny,nx,dps+1))
            maze[ny][nx] = 0
            cnt = dps+1
        
    # print(cnt)

print(cnt+1)