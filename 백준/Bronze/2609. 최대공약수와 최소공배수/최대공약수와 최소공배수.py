def uclide(max, min):
    if max%min == 0:
        return min
    save = max%min
    max = min
    min = save
    return uclide(max, min)


number = sorted(list(map(int,input().split())))

# print(number)
min, max = number[0], number[1]
# print(uclide(max, min))

small = uclide(max, min)
big = max*min/small

print(small)
print(int(big))