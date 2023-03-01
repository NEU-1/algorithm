import sys
from collections import deque
T = int(input())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().rstrip().split())

    visited = [False for i in range(10001)]
    que = deque()
    que.append([A,''])
    visited[A] = True

    while que:
        num, save = que.popleft()

        if num == B:
            print(save)
            break

        n = num * 2 % 10000
        if not visited[n]:
            visited[n] = True
            que.append([n, save + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            que.append([s, save + 'S'])

        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            que.append([l, save + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            que.append([r, save + 'R'])