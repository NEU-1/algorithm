for t in range(1, int(input())+1):
    num = int(input())
    end = -1
    for i in range(1, 10**6+1):
        if i**3 == num:
            end = i
            break
    print(f'#{t} {end}')