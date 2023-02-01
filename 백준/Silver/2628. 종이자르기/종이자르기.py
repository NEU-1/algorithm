x, y = map(int, input().split())
num = int(input())
x_list = []
y_list = []
for n in range(num):
    a, b = map(int, input().split())
    if a == 0:
        y_list.append(b)
    else:
        x_list.append(b)
x_list.append(x)
y_list.append(y)
x_list.sort()
y_list.sort()
# print(y_list)
x_save = [x_list[0]]
y_save = [y_list[0]]
for i in range(1, len(x_list)):
    x_save.append(x_list[i]-x_list[i-1])
for j in range(1, len(y_list)):
    y_save.append(y_list[j]-y_list[j-1])
print(max(x_save) * max(y_save))