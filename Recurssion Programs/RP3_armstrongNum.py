#armstrong Num

def arm(n):
    if n==0:
        return 0
    return (n%10)**(len(str(num)))+arm(n//10)
num=153
print('Armstrong num' if arm(num)==num else 'Not an Armstrong Num')
