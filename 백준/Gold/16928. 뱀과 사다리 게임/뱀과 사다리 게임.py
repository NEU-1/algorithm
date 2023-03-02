import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
up_down = {}
for _ in range(N+M):
    start, end = map(int, sys.stdin.readline().split())
    up_down[start] = end

def bfs():
    que = deque([(1, 0)])
    visited = [False] * 101 
    visited[1] = True

    while que:
        now, cnt = que.popleft()

        for i in range(1, 7):
            nxt = now + i

            if nxt <= 100 and not visited[nxt]:
                visited[nxt] = True
                if nxt in up_down:
                    nxt = up_down[nxt] 
                if nxt == 100: 
                    return cnt + 1
                que.append((nxt, cnt+1))

print(bfs())
