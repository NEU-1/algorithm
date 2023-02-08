A, B, V = map(int, input().split())
day = (V-A)//(A-B)
if (V-A)%(A-B) != 0:
    day += 1
day += 1
print(day)