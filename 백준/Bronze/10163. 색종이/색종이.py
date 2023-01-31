paper = int(input())
save_paper = []
for p in range(paper):
    save_paper.append(list(map(int,input().split())))
reverse_paper = save_paper[::-1]
check_paper = []
count = []
for pa in range(paper):
    for x in range(reverse_paper[pa][2]):
        for y in range(reverse_paper[pa][3]):
            check_paper.append((reverse_paper[pa][0]+x, reverse_paper[pa][1]+y))
    if pa == 0:
        set_paper = set(check_paper)
        count.append(len(set_paper))
    else:
        # print(check_paper)
        count.append(len(set(check_paper)-set_paper))
        # print(set_paper)
        set_paper = set_paper | set(check_paper)
revers_count = count[::-1]
print(*revers_count)

            





