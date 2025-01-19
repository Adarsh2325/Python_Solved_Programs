# To add all digits in a number using Functions

def add_dig(num,res=0):
    while num!=0:
        rem=num%10
        res=res+rem
        num=num//10
    return res
num=13
print(add_dig(num))
