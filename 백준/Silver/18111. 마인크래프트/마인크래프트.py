y, x, bag = map(int, input().split())
qube = [list(map(int, input().split())) for _ in range(y)]
up = 0
down = 256
# print(qube)
for i in qube:
    up = max(i) if max(i) > up else up
    down = min(i) if min(i) < down else down
check = []
# print(up, down)

def block(mid, bag):
    del_block = 0
    append_block = 0
    for q in qube:
        for p in q:
            if p > mid:
                del_block += p - mid
                bag += p - mid
            elif p < mid:
                append_block += mid - p
    if bag >= append_block:
        return del_block * 2 + append_block
    else:
        return 99999999


for mid in range(down, up+1):
    check.append(block(mid, bag))
check = check[::-1]

# print(check)
print(min(check), up - check.index(min(check)))
