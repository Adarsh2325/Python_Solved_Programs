# Program to check Given Number is Emirp Number or Not

num=11
dup=num
res=0
while num!=0:
    rem=num%10
    res=res*10+rem
    num=num//10
if dup!=res:
    for den in range(2,dup//2+1):
        if dup%den==0:
            print('It is not a Prime Num')
            break
    else:
        for deno in range(2,res//2+1):
            if res%deno==0:
                print('It is not a Prime Num')
                break
        else:
            print('It is an Emirp Number')
else:
    print('It is Not an Emirp Number')
       
         
            
