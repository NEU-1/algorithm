from collections import deque

N, K = map(int,input().split())

now = deque()
now.append((N, 0))
visited= [False] * 100001
visited[N] = True

while now:
    # print(now)
    start, cnt = now.popleft()

    if start == K:
        print(cnt)
        break

    for nxt in [start*2, start+1, start-1]:
        if 0 <= nxt <= 100000 and not visited[nxt]:
            now.append((nxt, cnt+1))
            visited[nxt] = True
