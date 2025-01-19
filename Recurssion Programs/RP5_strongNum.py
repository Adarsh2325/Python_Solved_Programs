def strong(n):
    if n==0:
        return 0
    return factorial(n%10)+strong(n//10)
def factorial(val):
    if val==0 or val==1:
        return 1
    return val*factorial(val-1)
num=145
print('Strong Num' if strong(num)==num else 'Not a Strong Num')
