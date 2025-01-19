# Program to Check the given number is Strong or Not

num=145
dup=num
res=0
while num!=0:
    rem=num%10
    fact=1
    for val in range(1,rem+1):
        fact=fact*val
    res=res+fact
    num=num//10
if res==dup:
    print('It is a Strong Number')
else:
    print('It is not a Strong Number')
    
    
