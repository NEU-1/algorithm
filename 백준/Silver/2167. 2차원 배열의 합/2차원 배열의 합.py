N, M = map(int, input().split())
qube = [list(map(int, input().split())) for n in range(N)]
K = int(input())
save = [[0]* (M+1) for _ in range(N+1)]
for y in range(1, N+1):
    for x in range(1, M+1):
        save[y][x] = qube[y-1][x-1] + save[y-1][x] + save[y][x-1] - save[y-1][x-1]
# print(save)
end = 0
for k in range(K):
    i, j, x, y = map(int,input().split())
    end = save[x][y] - save[i-1][y] - save[x][j-1] + save[i-1][j-1]
    print(end)

    # for Y in range(i-1, x):
    #     for X in range(j-1, y):
    #         # print(qube[Y][X])
    #         save += qube[Y][X]
    # # print(qube)
    # print(save)