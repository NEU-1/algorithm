def good_sequence(count):
    if count == N:
        return save
    for c in range(1,4):
        if is_valid(c, count):
            save[count] = c
            if good_sequence(count+1):
                return save
            save[count] = 0
    return False



def is_valid(c, count):
    save[count] = c
    for a in range(0, count):
        for b in range(1, min(a+2, count-a+1)):
            if save[a-b+1:a+1] == save[a+1:a+b+1]:
                return False
    return True





N = int(input())
save = [0]*N
result = good_sequence(0)
for i in range(N):
    print(result[i], end ='')
