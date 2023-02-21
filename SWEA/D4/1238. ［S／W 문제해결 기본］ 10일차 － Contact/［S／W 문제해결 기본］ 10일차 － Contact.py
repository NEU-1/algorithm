from collections import deque

for t in range(1, 11):
    num, start = map(int,input().split())
    save = list(map(int,input().split()))
    phone = [[] for _ in range(101)]
    for i in range(num//2):
        phone[save[i*2]].append(save[i*2+1])
    call_check = dict()
    visited = [False] * 101
    # print(phone)
    q = deque([(start)])
    call_check[start] = 0
    visited[start] = True
 
    while q:
        num = q.popleft()

        for c in phone[num]:
            if visited[c]:
                continue
            visited[c] = True
            q.append(c)
            call_check[c] = call_check[num] + 1
            # print(call_check)
    
    # print(call_check)
    k = 0
    v = 0
    for key, value in call_check.items():
        if value > v:
            v = value
            k = key
        elif value == v:
            k = max(k, key)
            
    
    print(f'#{t} {k}')




