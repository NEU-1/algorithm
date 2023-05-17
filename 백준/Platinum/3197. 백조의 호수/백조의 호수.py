import sys
from collections import deque

delta_row = [-1, 1, 0, 0] 
delta_col = [0, 0, -1, 1]

# 지도의 크기 입력 받기
rows, cols = map(int,sys.stdin.readline().split())

map = []

time_to_melt = [[0]*cols for _ in range(rows)]

def is_out_of_bounds(row, col, max_row, max_col):
    return not (0 <= row < max_row and 0 <= col < max_col)

def bfs(map, max_row, max_col, queue):
    while queue:
        current = queue.popleft()
        for i in range(4):
            new_row = current[0] + delta_row[i]
            new_col = current[1] + delta_col[i]
            if not is_out_of_bounds(new_row, new_col, max_row, max_col) and map[new_row][new_col] == 'X' and not visited[new_row][new_col]:
                queue.append([new_row, new_col, current[2]+1])
                time_to_melt[new_row][new_col] = current[2]+1
                visited[new_row][new_col] = 1
    return current[2]

def bfs_for_binary_search(min_time, max_time):
    answer = 0
    while min_time <= max_time:
        mid_time = (max_time + min_time) // 2
        queue = deque([[swans[0][0], swans[0][1]]])
        visited = [[0]*cols for _ in range(rows)]
        visited[swans[0][0]][swans[0][1]] = 1
        found_swan = False
        while queue:
            current = queue.popleft()
            for i in range(4):
                new_row = current[0] + delta_row[i]
                new_col = current[1] + delta_col[i]
                if swans[1][0] == new_row and swans[1][1] == new_col:
                    found_swan = True
                    break
                if not is_out_of_bounds(new_row, new_col, rows, cols) and time_to_melt[new_row][new_col] <= mid_time and not visited[new_row][new_col]:
                    queue.append([new_row, new_col])
                    visited[new_row][new_col] = 1
            if found_swan:
                break
        if found_swan:
            answer = mid_time
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
    return answer

for i in range(rows):
    map.append(list(sys.stdin.readline().strip()))

swans = []

queue = deque()
visited = [[0]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if map[i][j] == 'L' or map[i][j] == '.':
            if map[i][j] == 'L':
                swans.append([i,j])
            queue.append([i,j,0])
            visited[i][j] = 1

min_time = 0
max_time = bfs(map, rows, cols, queue)

print(bfs_for_binary_search(min_time, max_time))
