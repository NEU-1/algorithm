import sys

def update(i, value):
    while i <= N:
        fenwick_tree[i] += value
        i += (i & -i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += fenwick_tree[i]
        i -= (i & -i)
    return result

def find_next_card(value):
    left, right = 1, N
    while left < right:
        mid = (left + right) // 2
        if prefix_sum(mid) < value:
            left = mid + 1
        else:
            right = mid
    return left

input = sys.stdin.readline

N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
queries = list(map(int, input().split()))

fenwick_tree = [0] * (N + 1)

for card in cards:
    update(card, 1)

for q in queries:
    next_card_value = find_next_card(prefix_sum(q) + 1)
    print(next_card_value)
    update(next_card_value, -1)
