from collections import deque
import sys

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def destroy_cluster(grid, height, left, row_size, col_size):
    i, j = row_size - height, 0
    if left == 1:
        for k in range(col_size):
            if grid[i][k] == 'x':
                grid[i][k] = '.'
                j = k
                break
    else:
        for k in range(col_size-1, -1, -1):
            if grid[i][k] == 'x':
                grid[i][k] = '.'
                j = k
                break

    broken_minerals = deque()
    for dx, dy in DIRECTIONS:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < row_size and 0 <= nj < col_size:
            if grid[ni][nj] == 'x':
                broken_minerals.append((ni, nj))
    
    return broken_minerals

def search_and_fall(grid, x, y, row_size, col_size):
    q = deque()
    check = [[0]*col_size for _ in range(row_size)]
    fall_list = []
    q.append((x, y))
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == row_size - 1:
            return
        if grid[x+1][y] == '.':
            fall_list.append((x, y))
        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row_size and 0 <= ny < col_size:
                if grid[nx][ny] == 'x' and not check[nx][ny]:
                    check[nx][ny] = 1
                    q.append((nx, ny))
    fall_cluster(grid, check, fall_list, row_size, col_size)

def fall_cluster(grid, check, fall_list, row_size, col_size):
    k, flag = 1, 0
    while True:
        for i, j in fall_list:
            if i + k == row_size - 1 or (grid[i+k+1][j] == 'x' and not check[i+k+1][j]):
                flag = 1
                break
        if flag:
            break
        k += 1

    for i in range(row_size - 2, -1, -1):
        for j in range(col_size):
            if grid[i][j] == 'x' and check[i][j]:
                grid[i][j] = '.'
                grid[i+k][j] = 'x'

def print_grid(grid, row_size, col_size):
    for i in range(row_size):
        for j in range(col_size):
            print(grid[i][j], end='')
        print()

def main():
    r, c = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(r)]
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))

    broken_minerals = deque()
    left = 1
    for height in heights:
        broken_minerals.extend(destroy_cluster(grid, height, left, r, c))

        while broken_minerals:
            x, y = broken_minerals.popleft()
            search_and_fall(grid, x, y, r, c)

        left *= -1

    print_grid(grid, r, c)

if __name__ == "__main__":
    main()
