# Program to Check Whether the given Number is Tech Number or Not

num=81
if len(str(num))%2==0:
    fp=num//(10**(len(str(num))//2))
    sp=num%(10**(len(str(num))//2))
    if num==(fp+sp)**2:
        print('The given number is Tech Number')
    else:
        print('The given Number is Not A Tech Number')


