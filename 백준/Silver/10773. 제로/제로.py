K = int(input())
save = [0]
for k in range(K):
    num = int(input())
    if num == 0:
        save.pop(-1)
    else:
        save.append(num)
print(sum(save))