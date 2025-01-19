# Program to find GCD of 2 Numbers

num1=12
num2=24
if num1>num2:
    gcd=num2
else:
    gcd=num1
while True:
    if num1%gcd==0 and num2%gcd==0:
        print(gcd)
        break
    else:
        gcd=gcd-1
