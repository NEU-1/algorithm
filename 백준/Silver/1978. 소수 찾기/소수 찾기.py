count = int(input())
number = list(map(int,input().split()))
coun = 0

zero = [0] * (max(number)+1)
zero[0] = 1
zero[1] = 1
for num in range(2, max(number)+1):
    if zero[num] == 0:
        for one in range(num*2, max(number)+1, num):
            zero[one] = 1

for n in number:
    if zero[n] == 0:
        coun += 1

print(coun)