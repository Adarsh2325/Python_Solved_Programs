# Program to convert binary to integer

num=1001
pos=1
res=0
while num!=0:
    rem=num%10
    res=res+rem*pos
    num=num//10
    pos=pos*2
print(res)
