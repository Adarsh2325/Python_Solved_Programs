num=4
copy=1
for line in range(1,num+1):
    for col in range(line):
        print(copy,end=' ')
    print()
    copy=copy+2

print('------------------------------------')

num=4
copy=1
spaces=num-1
for line in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(line):
        print(copy,end=' ')
    print()
    copy=copy+1
    spaces=spaces-1

print('------------------------------------')

num=4
spaces=1
for line in range(num*2-1,0,-2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(line):
        print('*',end='')
    print()
    spaces=spaces+1
