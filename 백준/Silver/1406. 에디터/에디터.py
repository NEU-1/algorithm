from sys import stdin

start = list(stdin.readline().strip())
save = []
num = int(input())
for _ in range(num):
    order = list(map(str, input().split()))

    if order[0] == 'P':
        start.append(order[1])

    elif order[0] == 'L':
        if start:
            save.append(start.pop())
        else:
            continue
    elif order[0] == 'D':
        if save:
            start.append(save.pop())
        else:
            continue
    elif order[0] == 'B':
        if start:
            start.pop()
        else:
            continue

print(''.join(start + list(reversed(save))))