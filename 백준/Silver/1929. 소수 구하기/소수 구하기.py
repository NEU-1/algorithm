start, end = map(int,input().split())

number = list(range(2, end+1))
zero = [0]*(end+1)
# print(zero)
for num in number:
    if zero[num] == 0:
        for one in range(num*2, end+1, num):
            # print(one)
            # print(num)
            zero[one] = 1
        if end >= num >= start:
            print(num)
