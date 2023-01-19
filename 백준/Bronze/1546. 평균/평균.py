num = int(input())
a = list(map(int,input().split()))

max_a = max(a)
new_a = []
for i in a:
    new_a.append(i / max_a * 100)
avg = sum(new_a)/ num
print(avg)


