from itertools import combinations

def get_combination_sums(arr):
    comb_sums = []
    for i in range(len(arr) + 1):
        for subset in combinations(arr, i):
            comb_sums.append(sum(subset))
    return comb_sums

def solve(arr, S):
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left_sums = get_combination_sums(left)
    right_sums = get_combination_sums(right)

    left_sums.sort()
    right_sums.sort(reverse=True)

    left_idx, right_idx = 0, 0
    cnt = 0

    while left_idx < len(left_sums) and right_idx < len(right_sums):
        total = left_sums[left_idx] + right_sums[right_idx]
        if total == S:
            left_cnt, right_cnt = 1, 1
            left_idx += 1
            right_idx += 1

            while left_idx < len(left_sums) and left_sums[left_idx] == left_sums[left_idx - 1]:
                left_cnt += 1
                left_idx += 1

            while right_idx < len(right_sums) and right_sums[right_idx] == right_sums[right_idx - 1]:
                right_cnt += 1
                right_idx += 1

            cnt += left_cnt * right_cnt

        elif total < S:
            left_idx += 1
        else:
            right_idx += 1

    if S == 0:
        cnt -= 1

    return cnt

N, S = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(arr, S))
