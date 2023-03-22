def print_star(x, y, size):
    if size == 3:
        star[y][x] = "*"
        star[y+1][x-1] = star[y+1][x+1] = "*"
        for i in range(-2, 3):
            star[y+2][x+i] = "*"
        return

    print_star(x, y, size//2)
    print_star(x-(size//2), y+(size//2), size//2)
    print_star(x+(size//2), y+(size//2), size//2)

def check(N):
    global star
    star = [[" " for j in range(2*N-1)] for i in range(N)]
    print_star(N-1, 0, N)
    for i in range(N):
        print("".join(star[i]))

N = int(input())
check(N)
