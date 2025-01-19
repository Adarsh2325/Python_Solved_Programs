#Program To Add Even Digits in a Number

num=5678
evensum=0
while num!=0:
    rem=num%10
    if rem%2==0:
        evensum=evensum+rem
    num=num//10
print(evensum)
