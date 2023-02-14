def check(apart, y, x, cnt):
    # print(y,x)
    apart[y][x] = 0
    cnt += 1
    for y_, x_ in [[1,0],[-1,0],[0,1],[0,-1]]:
        if 0 <= y+y_ < num and 0 <= x+x_ < num and apart[y+y_][x+x_] == 1:
            cnt = check(apart, y+y_, x+x_, cnt)
    return cnt






num = int(input())
apart = [list(map(int, list(input()))) for _ in range(num)]

cnt = 0
home = []

for y in range(num):
    for x in range(num):
        if apart[y][x] == 1:
            cnt = check(apart, y, x, cnt)
            home.append(cnt)
            cnt = 0
home.sort()
print(len(home))
for i in home:
    print(i)

