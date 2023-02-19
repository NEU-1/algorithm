
def uclide(a,b):
    if a % b == 0:
        return b
    c = a % b
    (a, b) = (b, c)
    return uclide(a, b)

tree = int(input())
save = [0]
m = []
for _ in range(tree):
    num = int(input())
    m.append(num - save[-1])
    save.append(num)

save.pop(0)
m.pop(0)
m.sort()
check = m[0]
for n in range(1, len(m)):
    # print(check, n)
    if m[n] // check == 0:
        pass
    else:
        check = uclide(m[n], check)

# print(check, m)

end = ((save[-1] - save[0]) // check) - tree + 1
print(end)

