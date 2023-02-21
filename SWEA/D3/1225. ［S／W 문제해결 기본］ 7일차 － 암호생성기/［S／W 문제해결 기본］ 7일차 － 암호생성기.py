from collections import deque

for t in range(1, 11):
    _ = int(input())
    num = deque(map(int,input().split()))

    while num[-1] > 0:
        for i in range(1, 6):
            num.append(num.popleft()-i)
            if num[-1] <= 0:
                break
    num[-1] = 0
    print('#', end = '')
    print(t, *num)
