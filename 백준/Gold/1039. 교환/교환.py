from collections import deque

def bfs():
    Q = deque([(N, 0)]) 
    visited = [[0]*11 for _ in range(1000001)]
    max_value = -1 

    while Q:
        now, cnt = Q.popleft() 

        if cnt == K: 
            max_value = max(max_value, now) 
            continue

        str_now = str(now) 
        for i in range(len(str_now)):
            for j in range(i+1, len(str_now)):
                if i == 0 and str_now[j] == '0': 
                    continue
                swapped = str_now[:i] + str_now[j] + str_now[i+1:j] + str_now[i] + str_now[j+1:]
                next_num = int(swapped)

                if visited[next_num][cnt+1] == 0:
                    visited[next_num][cnt+1] = 1
                    Q.append((next_num, cnt+1)) 

    return max_value if max_value != -1 else -1 

N, K = map(int, input().split())
print(bfs())
