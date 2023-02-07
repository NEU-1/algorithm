while True:
    num = list(map(int, input().split()))
    num.sort()
    if num == [0,0,0]:
        break
    elif num[-1]**2 == num[0]**2+num[1]**2:
        print('right')
    else:
        print('wrong')