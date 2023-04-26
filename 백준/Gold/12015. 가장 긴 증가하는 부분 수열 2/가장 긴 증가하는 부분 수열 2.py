import sys
from bisect import bisect_left

def lis(arr):
    lis_arr = [arr[0]]

    for num in arr[1:]:
        if lis_arr[-1] < num:
            lis_arr.append(num)
        else:
            idx = bisect_left(lis_arr, num)
            lis_arr[idx] = num

    return len(lis_arr)

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

print(lis(sequence))
