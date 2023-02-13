num = int(input())
save = list(map(int, input().split()))

count = [0] * 2001
for i in save:
    count[i+1000] += 1

for j in range(1, 2001):
    count[j] += count[j-1]

sorted_a = [0] * num
for k in range(num-1, -1, -1):
    sorted_a[count[save[k]+1000]-1] = save[k]
    count[save[k]+1000] -= 1

for num in sorted(set(sorted_a)):
    print(num, end=' ')
