T = int(input())
for t in range(T):
    count = 0
    H, W, N = map(int, input().split())
    for w in range(1, W+1):
        for h in range(1, H+1):
            count += 1
            if count == N:
                print(f'{h*100 + w}')