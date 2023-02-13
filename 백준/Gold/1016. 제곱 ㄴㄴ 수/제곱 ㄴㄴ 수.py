import math
start, end = map(int, input().split())
check = [0] * (end - start + 1)
num = end - start
for i in range(2, int(end**0.5)+1):
        for j in range(math.ceil(start / (i**2)) * (i**2), end+1, i**2):
            check[j-start] = 1

print(check.count(0))
