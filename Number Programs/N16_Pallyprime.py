# Program to Check the given number is Palyprime or Not

num=11
dup=num
for den in range(2,num//2+1):
    if num%den==0:
        print('Not a Pallyprime')
        break
    else:
        res=0
        while num!=0:
            rem=num%10
            res=res*10+rem
            num=num//10
        if dup==res:
            print('It is a PallyPrime')
            break
        else:
            print('It is Not a Pallyprime')
        
