ids = list()
for _ in range(int(input())):
    a, b = input().split()
    ids.append((int(a),b))
    # print(ids)
    # ids[int(a)] = b
    # print(a)
# print(ids)
sort_id = sorted(ids, key=lambda x: x[0])
# print(sort_id)
for ids in sort_id:
    print(ids[0], ids[1])