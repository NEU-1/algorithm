from collections import deque

N = int(input())
apples = []
for _ in range(int(input())):
    a, p = map(int,input().split())
    apples.append((a, p))

turn = deque()
for _ in range(int(input())):
    t, u = input().split()
    turn.append((int(t), u))

dummy = [[0]*(N+1) for _ in range(N+1)]
dummy[1][1] = 1
snake = deque([(1,1)])

dy = [0,1,0,-1]
dx = [1,0,-1,0]
d, y, x = 0, 1, 1
time = 0

while True:
    time += 1
    # print(y, x, time, snake)
    y, x = y+dy[d], x+dx[d]

    if y < 1 or x < 1 or y > N or x > N:
        break
    elif (y, x) in snake:
        break

    snake.append((y, x))
    dummy[y][x] = 1

    if (y, x) in apples:
        apples.remove((y, x))
    else:
        snake.popleft()
        dummy[y][x] = 0
    
    if turn and time == turn[0][0]:
        if turn[0][1] == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        turn.popleft()
print(time)