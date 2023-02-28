n = int(input())
time = list(map(int, input().split()))
time.sort()  # 오름차순 정렬
save = 0
for i in range(n):
    save += time[i] * (n-i)
print(save)
