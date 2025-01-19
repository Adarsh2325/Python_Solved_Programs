# Program to Reverse a Number

num=12321
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)

num=12632
rev=0
dig=len(str(num))
pos=10**(dig-1)
while num!=0:
    rem=num%10
    rev=rev+rem*pos
    num=num//10
    pos=pos//10
print(rev)
