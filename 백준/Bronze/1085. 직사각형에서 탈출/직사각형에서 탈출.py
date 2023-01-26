x, y , x_max, y_max = map(int,input().split())

print(min(x, y, x_max-x, y_max-y))