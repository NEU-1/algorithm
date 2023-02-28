for t in range(1, 11):
    _ = input()
    table = [list(map(int,input().split())) for _ in range(100)]
    # print(table)
    check = False
    cnt = 0
    for x in range(100):
        for y in range(100):
            if table[y][x] == 1:
                check = True
            if table[y][x] == 2 and check == True:
                cnt += 1
                check = False
            if y == 99:
                check = False

    print(f'#{t} {cnt}')