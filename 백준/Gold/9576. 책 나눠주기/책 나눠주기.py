T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    book = []
    for j in range(M):
        book.append(list(map(int, input().split())))
    
    book.sort(key=lambda x: x[1])
    student = [0] * (N+1)
    cnt = 0
    
    for b in book:
        for s in range(b[0], b[1]+1):
            if student[s] == 0:
                student[s] = 1
                cnt += 1
                break
                
    print(cnt)
