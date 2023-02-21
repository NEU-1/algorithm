from collections import deque

N, K = map(int,input().split())
hp = deque(map(int,input().split()))
robots = deque([False]*N)

start = 0
end = N-1
cnt_zero = 0
step = 0

while cnt_zero < K:
    # print(start, end, robots, hp, step)

    hp.rotate(1)
    robots.pop()
    robots.appendleft(False)
    robots[end] = False

    for now in range(end-1,-1,-1):
        nxt = now+1
        if robots[now] and not robots[nxt] and hp[nxt] > 0:
            robots[nxt] = True
            robots[now] = False
            hp[nxt] -= 1
            if hp[nxt] == 0:
                cnt_zero += 1
        robots[end] = False
    
    if hp[start] > 0:
        hp[start] -= 1
        robots[start] = True
        if hp[start] == 0:
            cnt_zero += 1

    step += 1
print(step)
