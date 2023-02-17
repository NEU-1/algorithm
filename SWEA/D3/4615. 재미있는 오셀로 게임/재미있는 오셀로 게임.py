def 색칠 (dy, dx, color, qube):
    qube[dy][dx] = color
    y_ = [1,1,1,0,-1,-1,-1,0]
    x_ = [-1,0,1,1,1,0,-1,-1]
    for i in range(8):
        save = []
        for n in range(1, N):
            y = dy + y_[i]*n
            x = dx + x_[i]*n
            if qube[y][x] == 0:
                break
            elif qube[y][x] != color:
                save.append([y,x])
            else:
                while save:
                    yy, xx = save.pop()
                    qube[yy][xx] = color
                break
    return qube
            

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    qube = [[0]*(N+2) for _ in range(N+2)]
    mid = N//2
    
    qube[mid][mid] = qube[mid+1][mid+1] = 2
    qube[mid+1][mid] = qube[mid][mid+1] = 1
    for _ in range(M):
        y, x , color = map(int, input().split())
        색칠(y, x, color, qube)
        # print(qube)
        
    white = 0
    black = 0
    for q in qube:
        white += q.count(2)
        black += q.count(1)
    print(f'#{t} {black} {white}')