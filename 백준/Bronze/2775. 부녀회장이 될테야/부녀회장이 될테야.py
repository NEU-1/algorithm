def check(y, x):
    if y == 0 or x <= 1:
        return x
    elif apart[y][x] == 0:
        apart[y][x] = check(y-1, x) + check(y, x-1)
        return apart[y][x]
    else:
        return apart[y][x]




T = int(input())
for t in range(T):
    apart = [[0]*15 for _ in range(15)]
    floor = int(input())
    hosu = int(input())
    print(check(floor, hosu))
