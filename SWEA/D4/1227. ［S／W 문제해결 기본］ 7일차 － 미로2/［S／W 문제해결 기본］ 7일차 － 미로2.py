from collections import deque

for t in range(1,11):
    _ = input()
    maze = [list(str(input())) for _ in range(100)]
    runs = deque([(1,1)])
    # print(maze)

    y, x = 1, 1
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    fin = 0

    while runs:
        # print(runs)
        now = runs.popleft()
        y, x = now[0], now[1]
        # print(y, x)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            # print(ny, nx)
            if ny < 0 or nx < 0 or ny >= 100 or nx >= 100:
                continue
            elif maze[ny][nx] == '1':
                continue
            elif maze[ny][nx] == '3':
                fin = 1
                break
            elif maze[ny][nx] == '0':
                runs.append((ny,nx))
                # print(runs)
                maze[ny][nx] = 1
    
    print(f'#{t} {fin}')


    