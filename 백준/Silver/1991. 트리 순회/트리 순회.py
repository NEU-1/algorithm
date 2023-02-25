def VLR(node, tree):
    if node != '.':
        print(node, end="")
        VLR(tree[node][0], tree)
        VLR(tree[node][1], tree)

def LVR(node, tree):
    if node != '.':
        LVR(tree[node][0], tree)
        print(node, end="")
        LVR(tree[node][1], tree)

def LRV(node, tree):
    if node != '.':
        LRV(tree[node][0], tree)
        LRV(tree[node][1], tree)
        print(node, end="")

N = int(input())
tree = {}

for i in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

VLR('A', tree)
print()

LVR('A', tree)
print()

LRV('A', tree)
print()
