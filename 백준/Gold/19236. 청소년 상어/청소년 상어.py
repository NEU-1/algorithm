from copy import deepcopy

def check(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def find_fish(fish, fish_num):
    for x in range(4):
        for y in range(4):
            if fish[x][y][0] == fish_num:
                return [x, y]
    return False

def move_fish(x, y, fish):
    for fish_num in range(1, 17):
        now = find_fish(fish, fish_num)

        if not now:
            continue

        fx, fy = now
        fish_dir = fish[fx][fy][1]

        for z in range(8):
            nxt = (fish_dir + z) % 8
            dx, dy = d[nxt]
            nx, ny = fx + dx, fy + dy

            if not check(nx, ny) or (nx, ny) == (x, y):
                continue
            fish[fx][fy][1] = nxt
            fish[fx][fy], fish[nx][ny] = fish[nx][ny], fish[fx][fy]
            break

def dfs(x, y, eat, fish):
    global answer

    point = fish[x][y][0]
    eat += point
    fish[x][y] = [0, fish[x][y][1]]

    move_fish(x, y, fish)

    if answer < eat:
        answer = eat

    for i in range(1, 4):
        dx, dy = d[fish[x][y][1]]
        nx, ny = x + dx * i, y + dy * i

        if not check(nx, ny):
            continue

        if fish[nx][ny][0] == 0:
            continue

        temp = deepcopy(fish)
        dfs(nx, ny, eat, temp)

if __name__ == "__main__":
    d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    fish = []
    for i in range(4):
        save = list(map(int, input().split()))
        fish.append([[save[j*2], save[j*2+1]-1] for j in range(4)])

    answer = 0
    dfs(0, 0, 0, fish)
    print(answer)
