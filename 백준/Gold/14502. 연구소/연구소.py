from itertools import combinations
import copy

def virus_spread(lab, x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
            lab[nx][ny] = 2
            virus_spread(lab, nx, ny)

def safe_area(lab):
    return sum(row.count(0) for row in lab)

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

safe = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

max_safe = 0
for walls in combinations(safe, 3):
    danger = copy.deepcopy(lab)
    for x, y in walls:
        danger[x][y] = 1
    for x, y in virus:
        virus_spread(danger, x, y)
    max_safe = max(max_safe, safe_area(danger))

print(max_safe)
