x, y = map(int, input().split())
point = int(input())
save = []
all = (x+y)*2
for p in range(point+1):
    go, num = map(int, input().split())
    if go == 2:
        save.append(num)
    elif go == 4:
        save.append(x+y-num)
    elif go == 1:
        save.append(x+y+x-num)
    else:
        save.append(x+y+x+num)
# print(save)
start = save[-1]
hap = 0
for i in range(len(save)-1):
    hap +=min((start - save[i]+all)%all, (save[i] - start+all)%all)
print(hap)
