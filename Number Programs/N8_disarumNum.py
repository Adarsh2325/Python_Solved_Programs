# Program to Check Whether the given number is Disarum or Not

num=135
dup=num
res=0
pos=len(str(num))
while num!=0:
    rem=num%10
    res=res+rem**pos
    num=num//10
    pos=pos-1
if num==res:
    print('The given Number is Disarum Number ')
else:
    print('The given Number is Disarum Number ')
