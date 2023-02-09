def queen(y):
    if y == size:
        return 1

    count = 0
    for x in range(size):
        chess[y] = x
        if check(y):
            count += queen(y+1)
    return count

def check(y):
    for y_ in range(y):
        if chess[y] == chess[y_] or abs(chess[y] - chess[y_]) == y-y_:
            return False
    return True


size = int(input())
chess = [0]*size
y = 0
print(queen(y))
# print(chess)
