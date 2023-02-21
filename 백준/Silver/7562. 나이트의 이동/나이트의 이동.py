from collections import deque

def Knight(start, end, N):
    move = deque()
    y_, x_ = start
    move.append((y_, x_, 0))
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    while move:
        x, y, cnt = move.popleft()
        
        if (x, y) == end:
            return cnt
        
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                move.append((nx, ny, cnt+1))
                visited[nx][ny] = True
    
    return -1 

T = int(input())
for _ in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(Knight(start, end, N))
