def bell(start):
    distance[start] = 0
    
    for i in range(N):
        for j in range(2*M+W):
            cur_node = save[j][0]
            nxt_node = save[j][1]
            len_cost = save[j][2]

            if distance[cur_node] != INF and distance[nxt_node] > distance[cur_node] + len_cost:
                distance[nxt_node] = distance[cur_node] + len_cost

                if i == N-1:
                    return True
    return False

INF = int(1e9)
for _ in range(int(input())):
    N, M, W = map(int, input().split())
    save = []
    distance = [INF] * (N+1) 
    for _ in range(M):
        S, E, T = map(int, input().split())
        save.append((S, E, T))
        save.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        save.append((S, E, -T))

    for n in range(1, N+1):
        if distance[n] == INF:
            check = bell(n)
            if check:
                print("YES")
                break
    else:
        print("NO")
