from itertools import combinations





size, KFC_num = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(size)]
home = [(y,x) for y in range(size) for x in range(size) if city[y][x] == 1]
KFC_combinations = list(combinations([(y,x) for y in range(size) for x in range(size) if city[y][x] == 2], KFC_num))

최소_거리 = 999999
for KFCs in KFC_combinations:
    치킨_거리 = 0
    for 집 in home:
        최소_배달_거리 = 999999
        for KFC in KFCs:
            집_거리 = abs(집[0]-KFC[0]) + abs(집[1]-KFC[1])
            최소_배달_거리 = min(최소_배달_거리, 집_거리)
        치킨_거리 += 최소_배달_거리
    최소_거리 = min(최소_거리, 치킨_거리)

print(최소_거리)