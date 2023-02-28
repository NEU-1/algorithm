import sys
input = sys.stdin.readline

n = int(input())
check = [False] * 20

for _ in range(n):
    word, *num = input().split()
    num = int(*num)

    if word == 'add':
        check[num-1] = True

    elif word == 'remove':
        check[num-1] = False

    elif word == 'check':
        if check[num-1]:
            print(1)
        else:
            print(0)

    elif word == 'toggle':
        check[num-1] = not check[num-1]

    elif word == 'all':
        check = [True]*20

    elif word == 'empty':
        check = [False]*20
