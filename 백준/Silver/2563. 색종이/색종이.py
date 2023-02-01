N = int(input())
qube = [[0]*100]*100
# print(qube)
for n in range(N):
    x, y = map(int,input().split())
    for plus_y in range(10):
        qube[y+plus_y] = qube[y+plus_y][:x] + [1]*10 + qube[y+plus_y][x+10:]
count = 0
for i in qube:
    count += i.count(1)

print(count)