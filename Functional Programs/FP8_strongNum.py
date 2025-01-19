def factorial(n,fact=1):
    for val in range(1,n+1):
        fact=fact*val
    return fact
def strong(num,res=0):
    while num!=0:
        rem=num%10
        res=res+factorial(rem)
        num=num//10
    return res
num=145
print('Strong Number' if strong(num)==num else 'Not a strong number')
        
