def com(num, start, M):
    if M == 0:
        print(*num)
    else:
        for i in range(start, N):
            com(num + [save[i]], i, M-1)

N, M = map(int, input().split())
save = list(map(int, input().split()))
save.sort()
com([], 0, M)
