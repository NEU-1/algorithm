from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(h, w, board, keys):
    visited = [[False] * w for _ in range(h)]
    doors = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}
    q = deque([(0, 0)])
    visited[0][0] = True
    papers = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                cell = board[nx][ny]

                if cell == '*':
                    continue
                if 'A' <= cell <= 'Z':
                    if keys[ord(cell) - ord('A')]:
                        q.append((nx, ny))
                    else:
                        doors[cell].append((nx, ny))
                    continue
                if cell == '$':
                    papers += 1
                elif 'a' <= cell <= 'z':
                    keys[ord(cell) - ord('a')] = True
                    q.extend(doors[chr(ord(cell) - ord('a') + ord('A'))])

                q.append((nx, ny))

    return papers

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    board = ["." * (w + 2)] + ["." + input().strip() + "." for _ in range(h)] + ["." * (w + 2)]
    h += 2
    w += 2
    key_str = input().strip()
    keys = [False] * 26

    if key_str != '0':
        for key in key_str:
            keys[ord(key) - ord('a')] = True

    print(bfs(h, w, board, keys))
