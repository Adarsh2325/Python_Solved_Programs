def armstrong(n,power,res=0):
    while n!=0:
        rem=n%10
        res=res+rem**power
        n=n//10
    return res
n=153
print('Armstrong Num' if armstrong(n,len(str(n)))==n else ' Not an armstrong Num')
