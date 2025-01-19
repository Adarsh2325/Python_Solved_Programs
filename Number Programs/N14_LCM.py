# Program to find LCM of 2 Numbers

num1=3
num2=7
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
    else:
        lcm=lcm+1
        
