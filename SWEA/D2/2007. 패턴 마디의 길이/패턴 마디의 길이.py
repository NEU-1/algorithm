T = int(input())
for l in range(T):

    a = list(input())
    for i in range(1,30):
        if a[0:i] == a[i:i*2]:
            print(f'#{l+1} {len(a[0:i])}')
            break
        