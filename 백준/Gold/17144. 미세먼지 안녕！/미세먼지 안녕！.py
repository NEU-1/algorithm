R, C, T = map(int, input().split()) 
board = [list(map(int, input().split())) for _ in range(R)] 

for i in range(R):
    if board[i][0] == -1:
        cleaner_top = i
        cleaner_bottom = i+1
        break

def spread_dust():
    dusts = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                dusts.append((i, j, board[i][j]))

    for dust in dusts:
        r, c, amount = dust
        spread_amount = amount // 5
        spread_count = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                board[nr][nc] += spread_amount
                spread_count += 1
        board[r][c] -= (spread_amount * spread_count)

def operate_cleaner():
    for i in range(cleaner_top-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(cleaner_top):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 1, -1):
        board[cleaner_top][i] = board[cleaner_top][i-1]
    board[cleaner_top][1] = 0

    for i in range(cleaner_bottom+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    for i in range(R-1, cleaner_bottom, -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[cleaner_bottom][i] = board[cleaner_bottom][i-1]
    board[cleaner_bottom][1] = 0

for _ in range(T):
    spread_dust()
    operate_cleaner()

answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)
