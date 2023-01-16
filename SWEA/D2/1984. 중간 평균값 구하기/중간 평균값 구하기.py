T = int(input())

for t in range(1, T+1):
    num = list(map(int,input().split()))
    num.sort()
    del num[0]
    del num[len(num)-1]
    a = sum(num)/len(num)
    print(f'#{t} {int(round(a))}')