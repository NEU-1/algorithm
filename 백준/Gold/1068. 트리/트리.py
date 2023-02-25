def cnt_node(node, tree, del_node):
    if node == del_node:
        return 0
    
    count = 0
    for child in tree[node]:
        count += cnt_node(child, tree, del_node)
            
    if count == 0:
        return 1
    
    return count

N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(N)]
root = None

for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

if root == del_node:
    print(0)
else:
    print(cnt_node(root, tree, del_node))
