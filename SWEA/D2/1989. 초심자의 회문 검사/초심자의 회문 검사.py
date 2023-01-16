T = int(input())

for t in range(1, T+1):
    word = input()
    a = 1 if word == word[::-1] else 0
    print(f'#{t} {a}')