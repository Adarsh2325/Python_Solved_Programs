L=[-7,-2,2,3,5,11,19,36]
target=2
low=0
high=len(L)-1
while low<=high and (L[low]<=target<=L[high]):
    mid=(low+high)//2
    if L[mid]>target:
        high=mid-1
    elif L[mid]<target:
        low=mid+1
    elif L[mid]==target:
        print(mid)
        break
    else:
        print(-1)
print('-'*30)#------------------------------------------
def binary(L,target):
    low=0
    high=len(L)-1
    while low<=high and (L[low]<=target<=L[high]):
        mid=(low+high)//2
        if L[mid]>target:
            high=mid-1
        elif L[mid]<target:
            low=mid+1
        elif L[mid]==target:
            return mid
    return -1
L=[1,2,3,4,5]
target=3
print(binary(L,target))
print('-'*30)#------------------------------------------


    
