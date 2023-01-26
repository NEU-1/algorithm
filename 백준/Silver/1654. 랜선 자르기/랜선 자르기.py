
K, N = map(int,input().split())

lan_list = []
for r in range(K):
    lan_list.append(int(input()))
#-------------------------------------------

start = 1
end = max(lan_list)

# print(cm)
while start <= end:
    mid = (start+end)//2
    count = 0
    for c in lan_list:
        count += c // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)