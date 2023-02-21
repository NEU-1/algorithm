from collections import deque

x_, y_ = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(y_)]
check = deque()
for y in range(y_):
    for x in range(x_):
        if box[y][x] == 1:
            check.append((y, x, 0))

while check:
    # print()
    y, x, day = check.popleft()
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny < 0 or nx < 0 or ny >= y_ or nx >= x_:
            continue
        elif box[ny][nx] == 0:
            check.append((ny,nx,day+1))
            box[ny][nx] = 1
    # print(day)
cnt = 0
for b in box:
    if 0 in b:
        cnt += 1
if cnt != 0:
    print(-1)
else:
    print(day)
    



