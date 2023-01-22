student = []
for j in range(28):
    student.append(int(input()))

student_sorted = sorted(student)

student_set = set(student_sorted)
all_set = set(range(1, 31))

run = all_set - student_set
for i in sorted(run):
    print(i)