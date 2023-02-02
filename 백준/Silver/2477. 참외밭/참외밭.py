num = int(input())
m = []
for s in range(6):
    _, b = map(int,input().split())
    m.append(b)
max_x = max(m[0], m[2], m[4])
max_y = max(m[1], m[3], m[5])
min_x = m[m.index(max_y)-3]
min_y = m[m.index(max_x)-3]
print(((max_x*max_y) - (min_x*min_y))*num)

# 7
# 2 160
# 3 30
# 1 60
# 3 20
# 1 100
# 4 50