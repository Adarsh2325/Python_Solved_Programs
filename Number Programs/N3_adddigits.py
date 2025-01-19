# Program to Add all Digits in the given Number

num=36352
digSum=0
while num!=0:
    rem=num%10
    digSum=digSum+rem
    num=num//10
print(digSum)
