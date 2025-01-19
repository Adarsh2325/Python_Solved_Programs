def sq(n,res=0):
    while n!=0:
        rem=n%10
        res=res+rem**2
        n=n//10
    return res
def happy(num):
    while num>9:
        num=sq(num)
    return num==1 or num==7
num=19
print('Happy Num' if happy(num) else 'Not Happy Num')
