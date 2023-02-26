from collections import deque

def BFS(save):
    while save:
        y, x = save.popleft()
        now = color[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if not visited[ny][nx] and color[ny][nx] == now:
                save.append((ny,nx))
                visited[ny][nx] = True

def BFS_RG(save_rg):
    while save_rg:
        y, x = save_rg.popleft()
        now = color[y][x]
        # print(save_rg, visited_rg, now, y, x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if now == 'R' or now == 'G':
                if not visited_rg[ny][nx] and (color[ny][nx] == 'R' or color[ny][nx] == 'G'):
                    save_rg.append((ny,nx))
                    visited_rg[ny][nx] = True
            else:
                if not visited_rg[ny][nx] and color[ny][nx] == now:
                    save_rg.append((ny,nx))
                    visited_rg[ny][nx] = True

N = int(input())
color = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
visited_rg = [[False]*N for _ in range(N)]
cnt = 0
cnt_rg = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for y in range(N):
    for x in range(N):
        # print(y,x)
        if not visited[y][x]:
            save = deque()
            save.append((y,x))
            visited[y][x] = True
            cnt += 1
            BFS(save)
            if not visited_rg[y][x]:
                save_rg = deque()
                save_rg.append((y,x))
                visited_rg[y][x] = True
                cnt_rg += 1
                BFS_RG(save_rg)
print(cnt, cnt_rg)

'''
5
RRRRR
GGRRR
RRRRR
RRRRR
RRRRR
'''