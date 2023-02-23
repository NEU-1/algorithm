def LVR(n):
    if n > num:
        return
    LVR(n*2)
    print(word[n],end='')
    LVR(n*2+1)

    

for t in range(1, 11):
    num = int(input())
    word = [0]*(num+1)
    for _ in range(num):
        a, *b = input().split()
        word[int(a)] = b[0]
    print('#',end='')
    print(t,end=' ')
    LVR(1)
    print()
    
