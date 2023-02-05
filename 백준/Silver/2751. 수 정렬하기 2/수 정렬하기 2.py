import sys
run = int(sys.stdin.readline())
save = []
for r in range(run):
    save.append(int(sys.stdin.readline()))

save.sort()
for i in range(run):
    print(save[i])
