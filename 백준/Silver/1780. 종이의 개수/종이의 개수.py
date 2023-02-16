def cut(y, x, num):
    if check(y, x, num) != True:
        cut(y, x, num//3)
        cut(y,x+num//3,num//3)
        cut(y,x+num*2//3,num//3)
        cut(y+num//3,x,num//3)
        cut(y+num//3,x+num//3,num//3)
        cut(y+num//3,x+num*2//3,num//3)
        cut(y+num*2//3,x,num//3)
        cut(y+num*2//3,x+num//3,num//3)
        cut(y+num*2//3,x+num*2//3,num//3)

    return

def check(y_, x_, num):
    global zero, one, minus
    now = paper[y_][x_]
    for y in range(y_, y_+num):
        for x in range(x_, x_+num):
            if paper[y][x] != now:
                return False
    if now == 1:
        one += 1
    elif now == 0:
        zero += 1
    else:
        minus += 1
    return True

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
zero = 0
one = 0
minus = 0
cut(0,0,N)
print(minus)
print(zero)
print(one)