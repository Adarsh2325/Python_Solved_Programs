num=int(input('Enter the number : '))
print(num,type(num))
print('-'*30) #------------------------------------------------
L=[]
length=int(input('Enter the length of list : '))
for ele in range(length):
    ele=int(input('Enter the elements in the list: '))
    L.append(ele)
print(L)
print('-'*30) #-----------------------------------------------------
def convert(val):
    return int(val)
print(list(map(convert,input().split())))
print('-'*30) #-----------------------------------------------------
print(list(map(int,input().split())))
print('-'*30) #-----------------------------------------------------
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
print(list(map(lambda v1,v2 : v1+v2,L1,L2)))

