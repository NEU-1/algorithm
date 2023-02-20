def star(num, y, x):
    if num == 1:
        pattern[y][x] = '*'
        return
    number = num//3
    for y_ in range(3):
        for x_ in range(3):
            if y_ == 1 and x_ == 1:
                continue
            star(number, y + y_*number, x + x_*number)



num = int(input())
pattern = [[' ']*num for _ in range(num)]
star(num, 0, 0)
# print(pattern)
for p in pattern:
    print(''.join(p))