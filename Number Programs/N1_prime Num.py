# Program to Check given number is Prime Number or not

num=1
facount=0
for den in range(1,num+1):
    if num%den==0:
        facount=facount+1
if facount==2:
    print('It is Prime Number')
else:
    print('Its not a prime Number')
