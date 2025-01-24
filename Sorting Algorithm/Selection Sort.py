L=[10,3,9,7,-2,4]
for ind1 in range(len(L)-1):
    i=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[i]>L[ind2]:
            i=ind2
    L[i],L[ind1]=L[ind1],L[i]
print(L)
    




















 
