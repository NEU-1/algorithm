def com(num, start, M):
    if M == 0:
        print(*num)
    else:
        for i in range(start, N+1):
            com(num + [i], i+1, M-1)

N, M = map(int, input().split())
com([], 1, M)
