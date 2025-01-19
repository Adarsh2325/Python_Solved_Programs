def int(n,pos):
    if n==0:
        return 0
    return (n%2)*pos+int(n//2,pos*10)
num=14
print(int(num,1))
