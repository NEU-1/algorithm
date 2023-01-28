num = int(input())
save = dict()
for i in range(num+1):
    save.setdefault(i,0)
# print(save)
def fibonacci(num):
    if num <= 1:
        return num
    elif save[num] != 0:
        return save[num]
    else:
        save[num] = fibonacci(num-1) + fibonacci(num-2)
    return save[num]

print(fibonacci(num))