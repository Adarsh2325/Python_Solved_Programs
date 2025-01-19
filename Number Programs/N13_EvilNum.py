# Program to check given number is Evil or Odious

num=17
count=0
while num!=0:
    rem=num%2
    if rem==1:
        count=count+1
    num=num//2
if count%2==0:
    print ('The given number is Evil Number')
else:
    print ('The given number is Odious Number')
