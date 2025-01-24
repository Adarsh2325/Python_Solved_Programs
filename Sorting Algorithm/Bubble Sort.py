L=[10,42,8,23,6,2,12]
for ind1 in range(len(L)-1):
    for ind2 in range(len(L)-1-ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)   
print('-'*30) #------------------------------------------------
# Highest element in the list
L=[20,10,40,70,-10]
for ind1 in range(1):
    for ind2 in range((len(L)-1)-ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L[-1])
print('-'*30) #------------------------------------------------
# Highest element without using nested for loop
L=[20,10,40,70,-10]
high=L[0]
for ind in range(1,len(L)):
    if high<L[ind]:
        high=L[ind]
print(high)
print('-'*30) #------------------------------------------------
# Lowest element without using nested for loop
L=[20,10,40,70,-10]
low=L[0]
for ind in range(1,len(L)):
    if low>L[ind]:
        low=L[ind]
print(low)
