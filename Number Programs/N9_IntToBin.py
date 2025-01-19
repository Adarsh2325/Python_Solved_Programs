# Program to convert integer to binary

num=14
pos=1
res=0
while num!=0:
    rem=num%2
    res=res+rem*pos
    num=num//2
    pos=pos*10
print(res)
