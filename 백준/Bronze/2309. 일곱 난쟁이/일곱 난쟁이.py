dwarf = []
for d in range(9):
    dwarf.append(int(input()))

spy = sum(dwarf) - 100
# print(spy)
for x in range(8):
    for y in range(x+1,9):
        if dwarf[x] + dwarf[y] == spy:
            dwarf.pop(y)
            dwarf.pop(x)
            dwarf.sort()
            for i in dwarf:
                print(i)
            exit()

