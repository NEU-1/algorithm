from collections import deque

x_, y_, z_ = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(y_)] for _ in range(z_)]
# print(box)
check = deque()
for z in range(z_):
    for y in range(y_):
        for x in range(x_):
            if box[z][y][x] == 1:
                check.append((z, y, x, 0))

while check:
    # print()
    z, y, x, day = check.popleft()
    dy = [1,0,-1,0,0,0]
    dx = [0,1,0,-1,0,0]
    dz = [0,0,0,0,1,-1]

    for i in range(6):
        ny = y+dy[i]
        nx = x+dx[i]
        nz = z+dz[i]
        if ny < 0 or nx < 0 or nz < 0 or ny >= y_ or nx >= x_ or nz >= z_:
            continue
        elif box[nz][ny][nx] == 0:
            check.append((nz,ny,nx,day+1))
            box[nz][ny][nx] = 1
    # print(day)
cnt = 0
for b in box:
    for c in b:
        if 0 in c:
            cnt += 1
if cnt != 0:
    print(-1)
else:
    print(day)
    



