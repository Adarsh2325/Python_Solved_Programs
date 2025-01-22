L=[2,4,6,8,12,27]
target=8
low=0
high=len(L)-1
while low<=high and L[low]<=target<=L[high]:
    ind = int(low + ((high - low) * (target - L[low])) // (L[high] - L[low]))
    if L[ind]>target:
        high=ind-1
    elif L[ind]<target:
        low=ind+1
    elif L[ind]==target:
        print(ind)
        break
else:
    print(-1)
