def reverse(n,pos):
    if n==0:
        return 0
    return (n%10)*pos+reverse(n//10,pos//10)
num=123
print(reverse(num,10**(len(str(num))-1)))
