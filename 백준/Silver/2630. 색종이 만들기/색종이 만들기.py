def cut(y, x, num):
    if check(y, x, num) != True:
        cut(y, x, num//2)
        cut(y,x+num//2,num//2)
        cut(y+num//2,x,num//2)
        cut(y+num//2,x+num//2,num//2)
    return

def check(y_, x_, num):
    global white, blue
    now = paper[y_][x_]
    for y in range(y_, y_+num):
        for x in range(x_, x_+num):
            if paper[y][x] != now:
                return False
    if now == 1:
        blue += 1
    else:
        white += 1
    return True

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
start, end = 0, N-1
white = 0
blue = 0
cut(0,0,N)
print(white)
print(blue)