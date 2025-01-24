L=[10,2,14,-2,11,-4,20]
def quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[val for val in L[1: ] if pivot>val]
    right=[val for val in L[1: ] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
print(quick(L))

