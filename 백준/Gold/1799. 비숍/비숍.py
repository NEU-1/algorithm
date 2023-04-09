def bishop(index, cnt, is_black):
    global answer
    if index == len(save[is_black]):
        answer[is_black] = max(answer[is_black], cnt)
        return

    x, y = save[is_black][index]
    if not simul_1[x+y] and not simul_2[N-1-x+y]:
        simul_1[x+y] = simul_2[N-1-x+y] = True
        bishop(index+1, cnt+1, is_black)
        simul_1[x+y] = simul_2[N-1-x+y] = False

    bishop(index+1, cnt, is_black)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
save = [[], []]
simul_1, simul_2 = [False] * (2 * N), [False] * (2 * N)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            save[(i + j) % 2].append((i, j))

answer = [0, 0]
bishop(0, 0, 0)
bishop(0, 0, 1)

print(sum(answer))
