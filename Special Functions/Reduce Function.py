from functools import reduce
print(reduce(lambda v1,v2:v1+v2,range(1,6)))
print('-'*30) #----------------------------------
n=int(input("Enter a Number : "))
print(reduce(lambda v1,v2 : v1*v2,range(1,n+1),1))
print('-'*30) #----------------------------------
