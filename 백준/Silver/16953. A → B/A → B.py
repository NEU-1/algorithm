from queue import Queue

a, b = map(int, input().split())
q = Queue()
q.put((a, 1)) # (현재 수, 연산 수)

while not q.empty():
    x, cnt = q.get()
    if x == b:
        print(cnt)
        break
    if x*2 <= b:
        q.put((x*2, cnt+1))
    if int(str(x)+'1') <= b:
        q.put((int(str(x)+'1'), cnt+1))

if x != b:
    print(-1)
