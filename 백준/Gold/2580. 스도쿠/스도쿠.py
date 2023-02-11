
def save0(sdoku):
    save = []
    for y in range(9):
        for x in range(9):
            if sdoku[y][x] == 0:
                save.append([y,x])
    # save_list = [1]*len(save)
    return save

def check(y, x, sdoku):
    point = set(range(1, 10))
    point -= set(sdoku[y][j] for j in range(9))
    point -= set(sdoku[i][x] for i in range(9))
    sub_y, sub_x = (y//3)*3, (x//3)*3
    point -= set(sdoku[sub_y+i][sub_x+j] for i in range(3) for j in range(3))
    return list(point)


def 백트래킹(sdoku, save):
    if not save:
        return sdoku
    # 가능한 수를 빠르게 찾기
    save.sort(key=lambda z: len(check(z[0], z[1], sdoku)))
    y, x = save.pop(0)
    point = check(y, x, sdoku)
    for n in point:
        sdoku[y][x] = n
        if 백트래킹(sdoku, save):
            return sdoku
        sdoku[y][x] = 0
    save.insert(0, [y,x])
    return False




sdoku = [list(map(int,input().split())) for _ in range(9)]
# print(sdoku)
# run = find(sdoku)
save = save0(sdoku)

run = 백트래킹(sdoku, save)
for r in run:
    print(*r)

