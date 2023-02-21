from collections import deque

def check(draw):
    save = 0
    while draw:
        save += 1
        num = draw.popleft()
        y, x = num
        dy = [1,0,-1,0]
        dx = [0,-1,0,1]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or nx < 0 or ny >= y_ or nx >= x_:
                continue
            elif paper[ny][nx] == 1:
                draw.append((ny, nx))
                paper[ny][nx] = 0
    # print(save)
    return save

y_, x_ = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(y_)]

draw = deque()
cnt = 0
save = 0

for y in range(y_):
    for x in range(x_):
        # print(paper[y][x])
        if paper[y][x] == 1:
            paper[y][x] = 0
            draw.append((y,x))
            # print(draw)
            cnt += 1
            save = max(save, check(draw))
print(cnt)
print(save)
            

