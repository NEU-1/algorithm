T = int(input())

for t in range(1, T+1):
    a = 0
    for i in range(1, int(input())+1):
        num = (i*-1) if i%2 == 0 else i
        a += num
    print(f'#{t} {a}')