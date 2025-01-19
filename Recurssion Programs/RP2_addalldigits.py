# To add all digits in a Number

def add_dig(n):
    if n==0:
        return 0
    return n%10+add_dig(n//10)
n=5678
print(add_dig(n))
