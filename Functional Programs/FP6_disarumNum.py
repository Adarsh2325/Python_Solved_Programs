def disarum(n,power,res=0):
    while n!=0:
        rem=n%10
        res=res+rem**power
        power=power-1
        n=n//10
    return res
n=135
print('Disarum Num' if disarum(n,len(str(n)))==n else ' Not an Disarum Num')

