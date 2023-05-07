import sys

def find(x, parent):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x], parent)
        return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x != y:
        parent[y] = x
        return True
    return False

def main():
    input = sys.stdin.readline
    G = int(input())  
    P = int(input())  
    planes = [int(input()) for _ in range(P)]
    parent = [i for i in range(G + 1)]

    count = 0
    for plane in planes:
        docking_gate = find(plane, parent)
        if docking_gate == 0:
            break
        count += 1
        union(docking_gate - 1, docking_gate, parent)

    print(count)

if __name__ == "__main__":
    main()
