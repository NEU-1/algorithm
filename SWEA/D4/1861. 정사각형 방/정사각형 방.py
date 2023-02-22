from collections import deque

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def check(y, x):
    global cnt
    now = room[y][x]

    for i in range(4):
        ny = y+dy[i]   
        nx = x+dx[i]

        if 0 <= ny < num and 0 <= nx < num and room[ny][nx] == now+1:
            cnt+=1
            check(ny, nx)

for t in range(1, int(input())+1):
    num = int(input())
    room = [list(map(int,input().split())) for _ in range(num)]
    mx = num**2
    go = [0]*(mx+1)
    # print(room, visited)
    for y in range(num):
        for x in range(num):
            cnt = 1
            now = room[y][x]
            check(y, x)
            go[now] = cnt

    print(f'#{t} {go.index(max(go))} {max(go)}')



           