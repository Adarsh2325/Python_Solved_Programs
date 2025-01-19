def palindrome(n,res=0):
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
def pallyprime(num):
    if prime(num) and palindrome(num)==num:
        return 'It is a Pallyprime'
    return 'It is not a pallyprime'
num=11
print(pallyprime(num))
    
    
