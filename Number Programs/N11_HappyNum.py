# Program to Check Whether the given Number is Happy Number or Not

num=19
while num>9:
    res=0
    while num!=0:
        rem=num%10
        res=res+rem**2
        num=num//10
    num=res
if num==1 or num==7:
    print('The given number is Happy Number')
else:
    print('The given number is not a Happy Number')
