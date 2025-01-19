# Program to Check Whether the given number is Pallindrome or Not

num=1267621
dup=num
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if rev==dup:
    print(f'The Given Number {dup} is Pallindrome')
else:
    print('The Given Number is Not a Pallindrome')
    
