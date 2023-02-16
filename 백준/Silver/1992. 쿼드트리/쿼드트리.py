def cut(y, x, num):
    global save
    save = check(y, x, num)
    if save == False:
        save = '(' + cut(y, x, num//2) + cut(y,x+num//2,num//2) + cut(y+num//2,x,num//2) + cut(y+num//2,x+num//2,num//2) + ')'
    return save

def check(y_, x_, num):
    now = paper[y_][x_]
    for y in range(y_, y_+num):
        for x in range(x_, x_+num):
            if paper[y][x] != now:
                return False
    if now == 1:
        return '1'
    else:
        return '0'

N = int(input())
paper = [list(map(int,list(input()))) for _ in range(N)]
start, end = 0, N-1
white = 0
blue = 0
save = ''
cut(0,0,N)
print(save)