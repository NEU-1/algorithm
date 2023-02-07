T = int(input())
for t in range(T):
    ps = list(input())
    vps = []
    for p in ps:
        if p == '(':
            vps.append(-1)
        else:
            vps.append(1)
    if vps.count(-1) != vps.count(1):
        fin = 'NO'
    else:
        sum = 0
        for v in vps:
            sum += v
            if sum > 0:
                fin = 'NO'
                break
            else:
                fin = 'YES'
    print(fin)