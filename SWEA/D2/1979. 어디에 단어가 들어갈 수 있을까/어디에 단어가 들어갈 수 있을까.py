import copy

T = int(input())
for t in range(1, T+1):
    N,K = list(map(int,input().split())) # 범위값 입력
    num = 0
    count = 0
    # print(N,K)
    qube_x = [list(map(int,input().split())) for z in range(N)] 
    # 큐브 완성
    qube_y = copy.deepcopy(qube_x)
    # 큐브 카피
    # print(qube_x)
    for y in range(N): # 활동범위 설정 0~5
        if count == K:
            num += 1
            count = 0
        else:
            count = 0
        # print(y)
        for x in range(N): # 활동범위 설정 0~5
            if qube_x[y][x] == 1:
                qube_x[y][x] = 0
                count += 1
            else:
                if count == K:
                    num += 1
                    count = 0
                else:
                    count = 0
    for z in range(N): # 활동범위 설정 0~5
        if count == K:
            num += 1
            count = 0
        else:
            count = 0
        # print(y)
        for c in range(N): # 활동범위 설정 0~5
            if qube_y[c][z] == 1:
                qube_y[c][z] = 0
                count += 1
            else:
                if count == K:
                    num += 1
                    count = 0
                else:
                    count = 0
    if count == K:
                num += 1                      
    print(f'#{t} {num}')
