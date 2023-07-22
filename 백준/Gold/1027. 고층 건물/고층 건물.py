num = int(input())
building = list(map(int,input().split()))
radius = None
save_cnt = [0 for i in range(len(building))]

for i in range(len(building)):
    cnt_left = 0
    cnt_right = 0

    if i != 0:
        for j in range(i):
            check_radius = (building[i-j-1]-building[i])/(j+1)
            if cnt_left == 0 or check_radius > radius:
                radius = check_radius
                cnt_left += 1

    if i != -1:
        for k in range(i+1,len(building)):
            check_radius = (building[k]-building[i])/(k-i)
            if cnt_right == 0 or check_radius > radius:
                radius = check_radius
                cnt_right += 1

    save_cnt[i] = cnt_left + cnt_right
print(max(save_cnt))
        

