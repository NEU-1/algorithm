import sys
N = sys.stdin.readline()
number = [0]*10001
save = dict()
for _ in range(int(N)):
    number[int(sys.stdin.readline())] += 1

for n in range(10001):
    if number[n] != 0:
        for m in range(number[n]):
            print(n)