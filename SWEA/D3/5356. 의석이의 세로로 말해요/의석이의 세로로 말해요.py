T = int(input())
save = [list(input()) for _ in range(5*T)]
for t in range(0,len(save),5):
    print(f'#{t//5+1}',end=' ')
    for x in range(15):
        for y in range(t,t+5):
            if len(save[y]) == 0:
                continue
            print(save[y].pop(0),end='')
            # print(y,x)
    print()