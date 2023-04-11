import sys
sys.setrecursionlimit(100000)

def dfs(x, y, count):
    global max_count

    max_count = max(max_count, count)

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not visited[ord(board[nx][ny]) - 65]:
            visited[ord(board[nx][ny]) - 65] = True
            dfs(nx, ny, count + 1)
            visited[ord(board[nx][ny]) - 65] = False

r, c = map(int, input().split())
board = [input().strip() for _ in range(r)]
visited = [False] * 26
max_count = 0

visited[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)

print(max_count)
