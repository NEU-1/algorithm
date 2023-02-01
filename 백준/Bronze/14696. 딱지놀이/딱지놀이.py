num = int(input())
for n in range(num):
    _, *a = map(int, input().split())
    _, *b = map(int, input().split())
    a.sort(reverse=True)
    b.sort(reverse=True)
    # print(a,b)
    i = 0
    while a[i] == b[i]:
        i += 1
        if i == min(len(a), len(b))-1:
            break
    # print(a[i], b[i])
    if a[i] > b[i]:
        print('A')
    elif a[i] < b[i]:
        print('B')
    elif a[i] == b[i]:
        if len(a) > len(b):
            print('A')
        elif len(a) < len(b):
            print('B')
        else:
            print('D')
