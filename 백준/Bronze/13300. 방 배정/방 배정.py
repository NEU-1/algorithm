import math
count, num = map(int,input().split())
student = dict()
for c in range(count):
    ke, y = input().split()
    key = ke + y
    if key not in student:
        student[key] = 1
    else:
        student[key] += 1
# print(student)

count = 0
for s, t in student.items():
    count += math.ceil(t/num)

print(count)