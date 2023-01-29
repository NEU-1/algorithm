run = int(input())
for r in range(run):
    num, target = map(int,input().split())
    paper = list(map(int,input().split()))
    check = [0]*num
    check[target] = 1
    count = 0

    
    while True:
        if paper[0] == max(paper):
            count += 1
            if check[0] == 1:
                print(count)
                break
            else:
                del paper[0]
                del check[0]
        else:
            paper.append(paper[0])
            del paper[0]
            check.append(check[0])
            del check[0]
