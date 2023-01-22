t = int(input())
num = list(map(int, input().split()))
check = int(input())
count = 0

for i in num:
    if check == i:
        count += 1
print(count)
