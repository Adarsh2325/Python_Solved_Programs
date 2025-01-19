#disarum Num

def disarum(n,pow):
    if n==0:
        return 0
    return (n%10)**pow+disarum(n//10,pow-1)
num=135
print('Disarum num' if disarum(num,len(str(num)))==num else 'Not an Disatrum Num')
