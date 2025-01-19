def reverse(n,res=0):
    while n!=0:
        rem=n%10
        res=res*10+rem
        n=n//10
    return res
def prime(x):
    for den in range(2,x//2+1):
        if x%den==0:
            return False
        return True
num=13
dup=reverse(num)
print('Emirp Num' if dup!=num and prime(num) and prime(dup) else 'Not Emirp Num')
    
        
