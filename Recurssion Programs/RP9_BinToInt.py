def bin(n,pos):
    if n==0:
        return 0
    return (n%10)*2**pos+bin(n//10,pos+1)
num=1111
print(bin(num,0))
