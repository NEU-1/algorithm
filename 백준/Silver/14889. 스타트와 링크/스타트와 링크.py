
def team(num, save, s, start):
    # print(save)
    if len(start) == num//2:
        # print(start)
        link = list(set(range(num)) - set(start))
        # print(start, link)
        save = min(abs(check(start) - check(link)), save)
        # print(check(start), check(link))
        if save == 0:
            return save
        return save

    for n in range(s, num):
        start.append(n)
        save = team(num, save, n+1, start)
        start.pop()
    return save

def check(team):
    hap = 0
    for t in range(len(team)-1):
        for e in range(t+1, len(team)):
            # print(team)
            hap += stat[team[t]][team[e]]
    return hap




num = int(input())
stat = [list(map(int,input().split())) for _ in range(num)]

for y in range(num):
    for x in range(num):
        if x > y:
            stat[y][x] += stat[x][y]
        elif x < y:
            stat[y][x] = 0

# print(stat)
save = 999
start = []

save = team(num, save, 0, start)

print(save)