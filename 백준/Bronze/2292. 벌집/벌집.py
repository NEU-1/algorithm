num = int(input())
room = (num+4)//6
check = 1
count = 0
while room >= check:
    count += 1
    check += count
print(count+1)