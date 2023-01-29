import sys
from collections import Counter
num = int(int(sys.stdin.readline()))
num_list = []
for n in range(num):
    num_list.append(int(int(sys.stdin.readline())))
num_list.sort()

sum_num = round(sum(num_list)/num)
print(sum_num)

center_num = num_list[(num-1)//2]
print(center_num)

list_two = Counter(num_list).most_common(2)
if len(list_two) > 1:
    if list_two[0][1] == list_two[1][1]:
        print(list_two[1][0])
    else:
        print(list_two[0][0])
else:
    print(list_two[0][0])

range_num = num_list[-1]-num_list[0]
print(range_num)

# 하... 카운트 모스트...