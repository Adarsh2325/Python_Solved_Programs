#By using normal method
L=[14,15,17,20,10,11,10,0]
target=10
for ind in range(len(L)):
    if L[ind]==target:
        print(ind)
        break
else:
    print(-1)
print('-'*30)#------------------------------------------
#By using Functions
def linear(L,target):
    for ind in range(0,len(L)):
        if L[ind]==target:
            return ind
    return -1
L=[5,3,8,2,1,6,8]
target=8
print(linear(L,target))
print('-'*30) #------------------------------------------
#By using Recurssions
L=[4,3,2,2]
target=2
def linear(L,target,ind):
    if ind==L[ind]+1:
        return 
    if L[ind]==target:
            return ind
    return linear(L,target,ind+1)
print(linear(L,target,0))
print('-'*30)#------------------------------------------
        
    
    
