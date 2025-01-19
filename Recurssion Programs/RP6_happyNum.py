def sq(n):
    if n==0:
        return 0
    return (n%10)**2+sq(n//10)
def happy(val):
    if val<10:
        return val
    return happy(sq(val))
num=7
var=happy(num)
print('Happy Num' if var==1 or var==7 else 'Not Happy Num')
