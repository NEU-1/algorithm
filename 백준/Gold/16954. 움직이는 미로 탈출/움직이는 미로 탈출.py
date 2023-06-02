import sys
from collections import deque

input = sys.stdin.readline

wall_pos = set()
for i in range(8):
    temp = input().rstrip()
    for j in range(8):
        if temp[j] == '#':
            wall_pos.add((i, j))

queue = deque([(7, 0)])

result = 0

direction = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]

while queue and wall_pos:
    temp = set()
    for _ in range(len(queue)):
        r, c = queue.popleft()
        if (r, c) == (0, 7):
            print(1)
            exit(0)

        for nr, nc in direction:
            rr, cc = r + nr, c + nc
            if not (0 <= rr <= 7 and 0 <= cc <= 7) or (rr, cc) in wall_pos:
                continue
            temp.add((rr, cc))

    wall_update = set()
    for r, c in wall_pos:
        if r + 1 == 8:
            continue
        wall_update.add((r + 1, c))
    wall_pos = wall_update

    queue.extend(list(temp - wall_pos))

print(1 if not wall_pos and queue else 0)
