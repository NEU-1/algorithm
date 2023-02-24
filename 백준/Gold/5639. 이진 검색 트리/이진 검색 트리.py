import sys
sys.setrecursionlimit(10**6)

def tree(start, end):
    if start > end: 
        return
    
    root = save[start] 
    div = end + 1 

    for i in range(start+1, end+1):
        if save[i] > root:
            div = i
            break
        
    tree(start+1, div-1)
    tree(div, end)
    print(root)

save = []
while True:
    try:
        node = int(input())
    except:
        break
    save.append(node)
    
tree(0, len(save)-1)
