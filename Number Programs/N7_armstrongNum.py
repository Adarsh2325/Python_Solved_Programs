# Program to Check Whether the given number is Armstrong or Not

num=135
dup=num
arm=0
pos=len(str(num))
while num!=0:
    rem=num%10
    arm=arm+rem**pos
    num=num//10
if arm==dup:
    print('The Given Number is Armstrong Number')
else:
    print('The Given Number is Not Armstrong Number')

    
