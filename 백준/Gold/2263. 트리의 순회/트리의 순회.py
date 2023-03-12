import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_dict = {val: idx for idx, val in enumerate(inorder)}

def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    print(root, end=' ')

    root_idx = inorder_dict[root]

    left_size = root_idx - in_start

    solve(in_start, root_idx - 1, post_start, post_start + left_size - 1)

    solve(root_idx + 1, in_end, post_start + left_size, post_end - 1)

solve(0, n - 1, 0, n - 1)
