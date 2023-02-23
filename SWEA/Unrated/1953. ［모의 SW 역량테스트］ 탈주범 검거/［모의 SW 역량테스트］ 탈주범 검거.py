from collections import deque

def pipe(num):
    if num == 1:
        return [0,1,2,3]
    elif num == 2:
        return [0,2]
    elif num == 3:
        return [1,3]
    elif num == 4:
        return [1,2]
    elif num == 5:
        return [0,1]
    elif num == 6:
        return [0,3]
    elif num == 7:
        return [2,3]
    pass

for q in range(1, int(input())+1):
    Y, X, YY, XX, T = map(int,input().split())
    underground = [list(map(int,input().split())) for _ in range(Y)]
    visited = [[False for _ in range(X)] for _ in range(Y)]
    # print(underground)
    runrun = deque()
    runrun.append((YY,XX, 1))
    visited[YY][XX] = True
    cnt = 0

    while runrun:
        num = runrun.popleft()
        y, x, t = num
        # print(y,x)
        # print(runrun)
        if t == T+1:
            break
        cnt += 1
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]
        now = underground[y][x]
        move = pipe(now)
        for i in move:
            ny = y+dy[i]
            nx = x+dx[i]
            if Y>ny>=0 and X>nx>=0 and underground[ny][nx] != 0 and not visited[ny][nx]:
                check = pipe(underground[ny][nx])
                for j in check:
                    if ny+dy[j] == y and nx+dx[j] == x:
                        runrun.append((ny,nx, t+1))
                        visited[ny][nx] = True
        # print(y,x)
    print(f'#{q} {cnt}')





'''
1
5 6 2 1 3      
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''