import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

def check(배추밭, y, x):
    # print(y,x)
    배추밭[y][x] = 0
    for y_, x_ in [[1,0],[-1,0],[0,1],[0,-1]]:
        if 0 <= y+y_ < 세로 and 0 <= x+x_ < 가로 and 배추밭[y+y_][x+x_] == 1:
            check(배추밭, y+y_, x+x_)





T = int(input())
for _ in range(T):
    가로, 세로, 배추 = map(int, input().split())
    배추밭 = [[0 for _ in range(가로)] for _ in range(세로)]
    지렁이 = 0

    for _ in range(배추):
        x_, y_ = map(int,input().split())
        배추밭[y_][x_] = 1

    for y in range(세로):
        for x in range(가로):
            if 배추밭[y][x] == 1:
                check(배추밭, y, x)
                지렁이 += 1
    print(지렁이)

