T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    dragon_fly = [list(map(int,input().split())) for a in range(N)]
    save_sum = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            sum = 0
            for q in range(M):
                for p in range(M):
                    sum += dragon_fly[y+q][x+p]
            save_sum = max(save_sum,sum)
    print(f'#{t} {save_sum}')