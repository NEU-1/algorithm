num = []
for i in range(9):
    num.append(int(input()))
max_num = max(num)
index_num = num.index(max_num)
print(max_num)
print(index_num+1)