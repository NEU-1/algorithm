T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    max_home = 0 
    for y in range(N):
        for x in range(N):
            for k in range(1, N+2):
                cost = k**2 + (k-1)**2
                cnt = 0 
                for r in range(N):
                    for c in range(N):
                        if abs(y-r) + abs(x-c) < k and city[r][c] == 1:
                            cnt += 1
                if cnt*M >= cost:
                    if cnt > max_home: 
                        max_home = cnt

    print(f'#{t} {max_home}')
