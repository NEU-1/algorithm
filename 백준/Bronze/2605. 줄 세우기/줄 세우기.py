num = int(input())
change = list(map(int, input().split()))

student = list(range(1, num+1))
for n in range(num):
    # print(student.pop(n))
    target = student.pop(n)
    student.insert(n-change[n], target)
    # print(student)

print(*student)

