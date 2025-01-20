print('\n'.join(list(map(lambda val : '*'*val,range(1,5)))))
print('-'*30)
print('\n'.join(list(map(lambda val : '*'*val,range(4,0,-1)))))
print('-'*30)
print('\n'.join(list(map(lambda val : '*'*5,range(1,5)))))
print('-'*30)
def binary(num,pos=1,res=0):
    while num!=0:
        rem=num%2
        res=res+rem*pos
        num=num//2
        pos=pos*10
    return res
print(list(map(binary,range(10,21))))
print('-'*30)
print('\n'.join(list(map(lambda sp,st :sp*'   '+st*'* ',range(0,4),range(4,0,-1)))))
print('-'*30)
print('\n'.join(list(map(lambda sp,st :sp*'   '+st*'* ',range(3,-1,-1),range(1,5)))))
print('-'*30)
print('\n'.join(list(map(lambda sp,st :sp*'   '+st*'* ',range(3,-1,-1),range(1,8,2)))))
print('-'*30)
print('\n'.join(list(map(lambda num :num*(str(num)+' '),range(1,5)))))

