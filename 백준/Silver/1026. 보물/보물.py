num = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순으로, B는 내림차순으로 정렬
A.sort()
B.sort(reverse=True)

save = sum([A[i]*B[i] for i in range(num)])
print(save)
