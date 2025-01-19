def prime(n):
    if n>1:
        for val in range(2,n//2+1):
            if n%val==0:
                return 'Not a Prime Num'
                break
            return 'It is prime Num'
    else:
        return 'Not a Prime Num'
n=7
print(prime(n))

            
