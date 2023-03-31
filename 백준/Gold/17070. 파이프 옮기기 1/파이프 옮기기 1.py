
def move_pipe(y, x, d):
    if y == N-1 and x == N-1:
        return 1

    if dp[y][x][d] != -1:
        return dp[y][x][d]

    count = 0

    for k in range(3):
        if (d == 0 and k == 1) or (d == 1 and k == 0):
            continue

        ny, nx = y + dy[k], x + dx[k]

        if ny < 0 or ny >= N or nx < 0 or nx >= N or house[ny][nx]:
            continue

        if k == 2 and (house[y+1][x] or house[y][x+1]):
            continue

        count += move_pipe(ny, nx, k)

    dp[y][x][d] = count
    return count

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, 1, 1], [1, 0, 1]
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]

print(move_pipe(0, 1, 0))
