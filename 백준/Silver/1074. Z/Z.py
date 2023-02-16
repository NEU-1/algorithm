def Z(N, y, x):
    if N == 1:
        return y*2 + x

    point = 2**(N-1)

    if y < point and x < point:  
        return Z(N-1, y, x)
    elif y < point and x >= point:  
        return point**2 + Z(N-1, y, x-point)
    elif y >= point and x < point:  
        return 2 * point**2 + Z(N-1, y-point, x)
    else:  
        return 3 * point**2 + Z(N-1, y-point, x-point)

N, y, x = map(int, input().split())

print(Z(N, y, x))
