import sys

def cal_diff(points, n, cnt, idx, x_sum, y_sum):
    if idx == n:
        return float('inf')

    if cnt == n // 2:
        return (x_sum ** 2 + y_sum ** 2) ** 0.5

    no_choose = cal_diff(points, n, cnt, idx + 1, x_sum, y_sum)
    choose = cal_diff(points, n, cnt + 1, idx + 1, x_sum - 2 * points[idx][0], y_sum - 2 * points[idx][1])

    return min(no_choose, choose)

t = int(input())

for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    x_sum = sum(x for x, _ in points)
    y_sum = sum(y for _, y in points)

    result = cal_diff(points, n, 0, 0, x_sum, y_sum)
    print(result)
