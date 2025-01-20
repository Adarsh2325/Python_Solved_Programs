def even(val):
    if val%2==0:
        return True
print(list(filter(even,range(1,10))))
print('-'*30) #----------------------------------
def prime(val):
    for den in range(2,val//2+1):
        if val%den==0:
            return False
        return True
print(list(filter(prime,range(10,20))))
print('-'*30) #----------------------------------
def armstrong(n,res=0):
    dup=n
    pos=len(str(n))
    while n!=0:
        rem=n%10
        res=res+rem**pos
        n=n//10
    if res==dup:
        return True
print(list(filter(armstrong,range(1,51))))
print('-'*30) #----------------------------------
def happy(n):
    while n>9:
        res=0
        while n!=0:
            rem=n%10
            res=res+rem**2
            n=n//10
        n=res
    return n==1 or n==7
print(list(filter(happy,range(1,20))))
print('-'*30) #----------------------------------
print(list(filter(lambda val : val>5,[14,5,2,6,0])))
    
