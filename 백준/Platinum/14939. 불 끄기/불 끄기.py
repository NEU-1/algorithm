import sys

def toggle(x, y, grid):
    directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            grid[nx][ny] = not grid[nx][ny]

def solve(grid):
    min_clicks = float('inf')
    for bit in range(2**10):
        temp_grid = [row.copy() for row in grid]
        clicks = 0

        for col in range(10):
            if bit & (1 << col):
                toggle(0, col, temp_grid)
                clicks += 1

        for row in range(1, 10):
            for col in range(10):
                if temp_grid[row-1][col]:
                    toggle(row, col, temp_grid)
                    clicks += 1

        if all(not cell for row in temp_grid for cell in row):
            min_clicks = min(min_clicks, clicks)

    return min_clicks if min_clicks != float('inf') else -1

if __name__ == '__main__':
    grid = [[True if c == 'O' else False for c in sys.stdin.readline().strip()] for _ in range(10)]
    print(solve(grid))
