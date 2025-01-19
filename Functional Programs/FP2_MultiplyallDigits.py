# Multipy all digits in a given number

def mul_dig(n,res=1):
    while n!=0:
        rem=n%10
        res=res*rem
        n=n//10
    return res
n=26
print(mul_dig(n))
