from collections import deque
import sys
input = sys.stdin.readline

que = deque()
for _ in range(int(input())):
    word = input().split()
    w = word[0]
    if w == 'push':
        que.append(word[1])
    elif w == 'pop':
        print(-1) if len(que) == 0 else print(que.popleft())
    elif w == 'size':
        print(len(que))
    elif w == 'empty':
        print(1) if len(que) == 0 else print(0)
    elif w == 'front':
        print(-1) if len(que) == 0 else print(que[0])
    elif w == 'back':
        print(-1) if len(que) == 0 else print(que[-1])
        

        
