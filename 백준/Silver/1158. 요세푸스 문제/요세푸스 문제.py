N, K = map(int,input().split())
check = list(range(1, N+1))
count = 0
save = []
while len(check):
    count += (K-1)
    count %= len(check)
    save.append(str(check.pop(count)))
print("<", ", ".join(save), ">", sep="")

