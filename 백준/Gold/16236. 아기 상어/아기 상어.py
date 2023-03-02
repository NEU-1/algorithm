from collections import deque

n = int(input())  
sea = []  
for i in range(n):
    sea.append(list(map(int, input().split())))
    for j in range(n):
        if sea[i][j] == 9:  
            shark_x, shark_y = i, j
            sea[shark_x][shark_y] = 0  

def eat_fish():
    global shark_x, shark_y, shark_size, time, eat_cnt 
    visited = [[False] * n for _ in range(n)] 
    visited[shark_x][shark_y] = True
    que = deque([(shark_x, shark_y, 0)])
    fish = []  

    while que:
        x, y, dist = que.popleft()

        
        if 0 < sea[x][y] < shark_size:
            fish.append((x, y, dist))

        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:  
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True

                if sea[nx][ny] <= shark_size:
                    que.append((nx, ny, dist + 1))

    if not fish:
        return False

    fish.sort(key=lambda x: (x[2], x[0], x[1]))
    x, y, dist = fish[0]
    shark_x, shark_y = x, y
    sea[shark_x][shark_y] = 0 
    time += dist  
    eat_cnt += 1  

    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0

    return True

shark_size = 2  
time, eat_cnt = 0, 0  
while eat_fish():
    pass    
print(time) 