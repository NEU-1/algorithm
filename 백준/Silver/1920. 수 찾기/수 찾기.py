N = int(input())
A = list(map(int,input().split()))
A.sort()
# print(A)
M  = int(input())
m = list(map(int,input().split()))
# print(m)

for a in m:
    start = 0
    end = N-1
    while end - start != 1:
        mid = (start+end)//2
        if A[mid] >= a:
            end = mid
        else:
            start = mid
    # print(start)
    # print(end)
    # print(a)
    if a == A[start]:
        print(1)
    elif a == A[end]:
        print(1)
    else:
        print(0)